from MQTT import MQTTListenerBaseClass
from Conversation import Dialog


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content_nl = ('topic: ~topic35()\n'
                        'language: dun\n'
                        'concept:(Help) [help vraag]\n'
                        'u: (Ik heb hulp nodig) Ik hoor graag je vraag!\n'
                        'u: (Hoe gaat het?) Met mij gaat het perfect\n'
                        'u: (ik ben mijn pasje kwijt) Voor vragen over je pasje kan je naar de balie\n'
                        'u: (Ik weet niet waar mijn lokaal is) Op mijn tablet kan je je lokaal vinden\n'
                        'u: (Waar is de balie?) De balie is aan de linker kant van mij'
                        'u: (Waar ben ik?) Je bent in het Wibauthuis\n')

    topic_content_en = ('topic: ~topic41()\n'
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
    vocabularyNl = ['ik ben mijn pasje kwijt', 'Ik weet niet waar mijn lokaal is',
                    'Ik heb hulp nodig', 'Hoe gaat het?', 'Waar is de balie?', 'Waar ben ik?']

    # Speechrecognition
    vocabularyEn = ['I need your help', 'How are you doing?', 'I lost my school ID',
                    'I dont know where my classroom is', 'Where is the information desk?', 'Where am I?']

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        elif str(msg.payload) == 'terug':
            self.mirai.robotState.setPosture('open')
            self.mirai.Dialog.deactivateTopic(self.topic_content_nl)
        elif str(msg.payload) == 'dutch':
            self.mirai.robotState.setPosture('dialog')
            self.mirai.textToSpeech.setLanguage("Dutch")
            self.mirai.speechRecognition.setVocabulary(self.vocabularyNl)
            self.mirai.textToSpeech.say("selecteer een probleem of roep het naar mij")
            self.mirai.Dialog.activateTopic(self.topic_content_nl, "Dutch")

            # self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        elif str(msg.payload) == 'back':
            self.mirai.robotState.setPosture('open')
            self.mirai.Dialog.deactivateTopic(self.topic_content_en)
        elif str(msg.payload) == 'english':
            self.mirai.robotState.setPosture('dialog')
            self.mirai.textToSpeech.setLanguage("English")
            self.mirai.speechRecognition.setVocabulary(self.vocabularyEn)
            self.mirai.textToSpeech.say("select a problem or ask me")
            self.mirai.Dialog.activateTopic(self.topic_content_en, "English")
