import paho.mqtt.client as mqtt
import threading

class MQTTListener(object):
    client = None
    def __init__(self, hostname):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        thread = threading.Thread(target=self.start())
        thread.start()
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        client.subscribe("$SYS/#")

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def start(self):
        self.client.connect("azsx.nl", 1883, 60)
        self.client.loop_forever()
listener = MQTTListener('azsx.nl')