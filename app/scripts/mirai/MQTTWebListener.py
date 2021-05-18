from MQTT import MQTTListenerBaseClass
import time


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content2 = ('topic: ~topic3()\n'
                      'language: enu\n'
                      'proposal: Kan ik je ergens mee helpen\n'
                        'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) waarmee kan ik je helpen .\n'
                        'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                        'u2: ([lokaal kamer klas ]) pak de linker lift .\n'
                        'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        elif str(msg.payload) == 'dutch':
            self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        #if str(msg.payload) == 'english':
            #self.mirai.ENGP.askForHelp()























    def q0(self):
        print ("ben bij vraag 4")
        #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/hoofdpagina.html")
        self.mirai.textToSpeech.say("heb je nog meer vragen")


        self.mirai.speechRecognition.startSpeecheRecognition()
        while not (self.mirai.speechRecognition.recognizeWord() == 'ja' or self.mirai.speechRecognition.recognizeWord() == 'nee'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'ja':
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'nee':
            self.mirai.textToSpeech.say("okey fijne dag nog")
            self.mirai.textToSpeech.stop()

    def q3(self):
        print ("ben bij vraag 3")
        time.sleep(1)
        self.mirai.textToSpeech.say("heb je vragen over je hva pas? ")
        while not (self.mirai.speechRecognition.recognizeWord()== 'ja' or self.mirai.speechRecognition.recognizeWord()):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'ja':
            self.mirai.textToSpeech.say("hiervoor verwijz ik je door naar de balie ")
            #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/pasje")
            time.sleep(3)
            self.q0()

        if self.mirai.speechRecognition.recognizeWord() == 'nee':
            self.mirai.textToSpeech.say("dan weet ik het ook niet succes ")


    def q2(self):
        print ("ben bij vraag 2")
        time.sleep(1)
        self.mirai.textToSpeech.say("wil je weten waar je lokaal is? ")

        while not (self.mirai.speechRecognition.recognizeWord() == 'ja' or self.mirai.speechRecognition.recognizeWord() == 'nee'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'ja':
            self.mirai.textToSpeech.say("typ op het tablet je lokaal nummer ")
            #tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/lokaal zoeken.html")
            time.sleep(3)
            self.q0()

        if self.mirai.speechRecognition.recognizeWord() == 'nee':
            self.q3()

    def q1(self):

        print ("ben bij vraag 1")
        time.sleep(1)
        self.mirai.textToSpeech.say("wil je weten waar je bent ")

        self.mirai.speechRecognition.recognizeWord()
        while not (self.mirai.speechRecognition.recognizeWord() == 'ja' or self.mirai.speechRecognition.recognizeWord() == 'nee'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'ja':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat")
            #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/plattegrond.html")
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'nee':
            self.q2()

    def askForHelp (self):
        self.mirai.speechRecognition.setLanguage("Dutch")
        self.mirai.speechRecognition.startSpeecheRecognition()



        print ("ben bij vraag 0")
        self.mirai.textToSpeech.say("kan ik je ergens mee helpen")


        while not (self.mirai.speechRecognition.recognizeWord() == 'ja' or self.mirai.speechRecognition.recognizeWord() == 'nee'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'ja':
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'nee':
            self.mirai.textToSpeech.say("okey fijne dag nog")





