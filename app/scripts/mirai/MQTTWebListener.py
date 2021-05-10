from MQTT import MQTTListenerBaseClass


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        if str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        if str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        if str(msg.payload) == 'dutch':
            self.mirai.dutchP.askForHelp()

        if str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        if str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        if str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        if str(msg.payload) == 'english':
            self.mirai.ENGP.askForHelp()



