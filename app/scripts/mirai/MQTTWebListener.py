from MQTT import MQTTListenerBaseClass
from Conversation import Dialog


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: dun\n'
                       'concept:(Help) [help vraag]\n'
                       'u: ([Ik heb hulp nodig. "Kan je me helpen?"]) Waar kan ik je mee helpen?\n'
                       'u: (Mijn pasje [werkt "doet het"] niet) Voor problemen met je pasje kan je terecht bij de '
                       'balie\n '
                       'u: (Waar is de balie?) Welkom leerling, de balie is aan de linker kant.\n'
                       'u: (Hoe gaat het?) Gaat je niks aan\n'
                       'u: ([Waar "Hoe"] kan ik mijn lokaal vinden) Op mijn tablet kan je de route vinden naar elk '
                       'lokaal.\n '
                       'u: (Waar kan ik eten [halen? "kopen?"]) Achter mij is een kantine waar eten verkocht wordt.\n'
                       'u: (Goede middag) Goede middag, veel succes tijdens je les!\n'
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) You touched my head!\n')

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        elif str(msg.payload) == 'dutch':
            self.mirai.textToSpeech.say("selecteer een probleem of roep het naar mij")
            self.mirai.Dialog.activateTopic(self.topic_content_1," Dutch")

            #self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        if str(msg.payload) == 'english':
            self.mirai.textToSpeech.say("select a problem or ask me")
            #self.mirai.ENGP.askForHelp()
