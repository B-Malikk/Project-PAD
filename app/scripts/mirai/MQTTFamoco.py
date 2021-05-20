import paho.mqtt.client as mqtt
import threading
import json
from MQTT import MQTTListenerBaseClass
import math
from datetime import datetime

EVENT_NORMAL = 0
EVENT_SUCCESS = 1
EVENT_ERROR = -1


class FamacoEventDetection(object):
    pastReadings = []
    MAX_BUFFER_SIZE = 100

    lastEvent = 0
    lastEventChange = None  # datetime.utcnow()

    callbackObject = None

    def __init__(self, callbackObject):
        self.callbackObject = callbackObject

    def process(self, value):
        value = int(math.ceil(value / 5)) * 5  # rounds value up to the nearest 5

        self.addReading(value)
        if not self.lastEventChange:
            self.setEvent(EVENT_NORMAL)

        if len(self.pastReadings) > self.MAX_BUFFER_SIZE:
            self.pastReadings.pop(0)

        if len(self.pastReadings) > 20:
            if value > self.getMode() and self.lastEvent == EVENT_NORMAL and self.shouldFireEvent(value):
                self.setEvent(EVENT_ERROR)
            elif value < self.getMode() and self.lastEvent == EVENT_NORMAL and self.shouldFireEvent(value):
                self.setEvent(EVENT_SUCCESS)
            elif self.lastEvent != EVENT_NORMAL and value == self.getMode() and self.shouldFireEvent(value):
                self.setEvent(EVENT_NORMAL)
            elif self.lastEvent != EVENT_NORMAL and value != self.getMode() and self.shouldFireEvent(value):
                diff = datetime.utcnow() - self.lastEventChange
                if diff.seconds > 10:

                    # Empty buffer
                    self.pastReadings = []

                    # Fill buffer
                    for i in range(20):
                        self.addReading(value)

                    self.setEvent(EVENT_NORMAL)

    def shouldFireEvent(self, value):
        values = [x['value'] for x in self.pastReadings[-4:-1]]
        lastValue = value
        for value in values:
            if lastValue != value:
                return False
        return True

    def getMode(self):
        list = [x['value'] for x in self.pastReadings]
        return max(set(list), key=list.count)

    def addReading(self, value):
        self.pastReadings.append({'time': datetime.utcnow(), 'value': value})

    def setEvent(self, event):
        self.lastEventChange = datetime.utcnow()
        self.lastEvent = event
        if event == EVENT_ERROR:
            self.callbackObject.on_error()
        elif event == EVENT_SUCCESS:
            self.callbackObject.on_success()


class MQTTFamoco(object):
    client = None
    hostname = 'mqtt.hva-robots.nl'
    topic = 'dekkerm54/scan'
    client_id = 'dekkerm54_pas_sub'
    username = 'dekkerm54'
    password = 'En6Gd6CEZqxTSAQ4ROyn'

    def __init__(self, mirai):
        self.mirai = mirai
        self.client = mqtt.Client(client_id=self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.eventDetection = FamacoEventDetection(self)

        thread = threading.Thread(target=self.start)
        thread.start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        self.on_event(msg)

    def start(self):
        self.client.username_pw_set(self.username, self.password)
        self.client.connect(self.hostname, 1883, 60)
        self.client.loop_forever()

    def on_event(self, msg):
        try:
            data = json.loads(msg.payload)
            value = int(math.ceil(data['ldr'] / 5)) * 5  # rounds value up to the nearest 5
            self.eventDetection.process(value)
        except Exception as e:
            print(e.message)
            pass

    def publish(self, payload=None):
        self.client.publish(self.topic, payload)

    def on_error(self):
        if self.mirai:
            self.mirai.motion.setStiffnesses(1.0)
            self.mirai.textToSpeech.say("Er ging iets mis.")

    def on_success(self):
        if self.mirai:
            self.mirai.motion.setStiffnesses(1.0)
            self.mirai.textToSpeech.say("Welkom.")
            self.mirai.motion.scanner()
            if self.mirai:
                self.mirai.motion.setAngles("RElbowRoll", 0, 4)


if __name__ == "__main__":
    listener = MQTTFamoco(None)
