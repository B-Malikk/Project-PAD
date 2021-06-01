from MQTT import MQTTListenerBaseClass
from Conversation import Dialog


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content_nl = ('topic: ~topic36()\n'
                        'language: dun\n'
                        'concept:(Help) [help vraag]\n'
                        'u: (Ik heb hulp nodig) Ik hoor graag je vraag!\n'
                        'u: (Hoe gaat het?) Met mij gaat het perfect\n'
                        'u: (ik ben mijn pasje kwijt) Voor vragen over je pasje kan je naar de balie\n'
                        'u: (Ik weet niet waar mijn lokaal is) Op mijn tablet kan je je lokaal vinden\n'
                        'u: (Waar is de balie?) De balie is aan de linker kant van mij\n'
                        'u: (Waar ben ik?) Je bent in het Wibauthuis\n'
                        'u: (sterf) Val dood\n')

    topic_content_en = ('topic: ~topic42()\n'
                        'language: enu\n'
                        'concept:(Help) [help question]\n'
                        'u: (I need your help) I would love to help you!\n'
                        'u: (How are you doing?) I am doing amazing.\n'
                        'u: (I lost my school ID) You can talk to someone at the information desk about your school '
                        'ID\n '
                        'u: (I dont know where my classroom is) You can find the route to your classroom on my tablet\n'
                        'u: (Where is the information desk?) The information desk is on my left\n'
                        'u: (Where am I?) You are in the Wibauthouse\n')

    # Speechrecognition
    vocabularyNl = ['ik ben mijn pasje kwijt', 'Ik weet niet waar mijn lokaal is','sterf',
                    'Ik heb hulp nodig', 'Hoe gaat het?', 'Waar is de balie?', 'Waar ben ik?']

    # Speechrecognition
    vocabularyEn = ['I need your help', 'How are you doing?', 'I lost my school ID',
                    'I dont know where my classroom is', 'Where is the information desk?', 'Where am I?']

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.sayAnimated("ik verwijs je door naar de balie.", mode='random')
            self.mirai.motion.point()
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.sayAnimated("vull alleen je lokaal nummer in.", mode='random')
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.sayAnimated("je bent nu in het HVA Wibauthuis aan de wibautstraat.", mode='random')
        elif str(msg.payload) == 'terug1':
            self.mirai.robotState.setPosture('open')
            self.mirai.Dialog.deactivateTopic(self.topic_content_nl)
        elif str(msg.payload) == 'dutch':
            self.mirai.robotState.setPosture('dialog')
            self.mirai.textToSpeech.setLanguage("Dutch")
            self.mirai.speechRecognition.setVocabulary(self.vocabularyNl,True)
            self.mirai.textToSpeech.sayAnimated("selecteer een probleem of roep het naar mij", mode='random')
            self.mirai.Dialog.activateTopic(self.topic_content_nl, "Dutch")

            # self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.sayAnimated("I will refer you to the counter", mode='random')
            self.mirai.motion.point()
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.sayAnimated("you are now in the HVA Wibauthuis on the wibautstraat", mode='random')
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.sayAnimated("only enter your classroom number", mode='random')
        elif str(msg.payload) == 'back1':
            self.mirai.robotState.setPosture('open')
            self.mirai.Dialog.deactivateTopic(self.topic_content_en)
        elif str(msg.payload) == 'english':
            self.mirai.robotState.setPosture('dialog')
            self.mirai.textToSpeech.setLanguage("English")
            self.mirai.speechRecognition.setVocabulary(self.vocabularyEn,True)
            self.mirai.textToSpeech.sayAnimated("select a problem or ask me", mode='random')
            self.mirai.Dialog.activateTopic(self.topic_content_en, "English")
