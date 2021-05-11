import paho.mqtt.client as mqtt
import threading


class MQTTListenerBaseClass(object):
    client = None
    hostname = 'azsx.nl'
    topic = 'topic'

    def __init__(self, mirai):
        self.mirai = mirai
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
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
        self.client.connect(self.hostname, 1883, 60)
        self.client.loop_forever()

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload) + " (you should override the on_event method)")

