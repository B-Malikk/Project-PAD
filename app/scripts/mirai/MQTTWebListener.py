from MQTT import MQTTListenerBaseClass


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
