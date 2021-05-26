from MQTT import MQTTListenerBaseClass
from Conversation import Dialog


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content_1 = ('topic: ~topic23()\n'
                       'language: dun\n'
                       'concept:(Help) [help vraag]\n'
                       # 'u: (I [want "would like"] {some} _~food) Sure! You must really like $1 .\n'
                       'u: (kaas) Gaat je niks aan\n'
                       'u: (help mij) Nee\n'
                       'u: (ik ben mijn pasje kwijt) ga naar de balie\n'
                       'u: (Ik weet niet waar mijn lokaal is) Op mijn tablet kan je je lokaal vinden\n'
                       'u: (Waar ben ik) Je bent in het wibauthuis\n')

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        elif str(msg.payload) == 'terug':
            self.mirai.Dialog.deactivateTopic(self.topic_content_1)
        elif str(msg.payload) == 'dutch':
            self.mirai.textToSpeech.setLanguage("Dutch")
            self.mirai.textToSpeech.say("selecteer een probleem of roep het naar mij")
            self.mirai.Dialog.activateTopic(self.topic_content_1," Dutch")

            #self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        elif str(msg.payload) == 'back':
            pass
        elif str(msg.payload) == 'english':
            self.mirai.textToSpeech.setLanguage("English")
            self.mirai.textToSpeech.say("select a problem or ask me")
