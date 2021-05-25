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
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) niet aanraken!\n')

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.robotState.setPosture('pass')
            self.mirai.motion.point()
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
            self.mirai.robotState.setPosture('open')
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.sayAnimated("vull alleen je lokaal nummer in.", mode= 'random')
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.sayAnimated("je bent nu in het HVA Wibauthuis aan de wibautstraat.", mode= 'random')
        elif str(msg.payload) == 'dutch':
            self.mirai.textToSpeech.sayAnimated("selecteer een probleem of roep het naar mij", mode= 'random')
            self.mirai.Dialog.activateTopic(self.topic_content_1," Dutch")

            #self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.robotState.setPosture('card')
            self.mirai.motion.point()
            self.mirai.textToSpeech.sayAnimated("I will refer you to the counter.", mode= 'random')
            self.mirai.robotState.setPosture('open')
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.sayAnimated("you are now in the HVA Wibauthuis on the wibautstraat.", mode= 'random')
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.sayAnimated("only enter your classroom number.", mode= 'random')
        if str(msg.payload) == 'english':
            self.mirai.textToSpeech.sayAnimated("select a problem or ask me", mode= 'random')
            #self.mirai.ENGP.askForHelp()
