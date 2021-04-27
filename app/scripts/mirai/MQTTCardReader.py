from MQTT import MQTTListenerBaseClass

class MQTTCardReader(MQTTListenerBaseClass):
    topic = 'Mirai/card/#'
    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == 'Mirai/card/scan':
            pass

reader = MQTTCardReader(None)
reader.start()