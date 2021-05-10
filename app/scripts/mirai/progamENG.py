from mirai._mirai import Mirai
import time

class engProgram(object):

    def q0(self):
        print ("ben bij vraag 4")
        #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/hoofdpagina.html")
        self.mirai.textToSpeech.say("do you have any more questions")


        self.mirai.speechRecognition.startSpeecheRecognition()
        while not (self.mirai.speechRecognition.recognizeWord() == 'yes' or self.mirai.speechRecognition.recognizeWord() == 'no'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'yes':
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'no':
            self.mirai.textToSpeech.say("okey have a nice day")
            self.mirai.textToSpeech.stop()

    def q3(self):
        print ("ben bij vraag 3")
        time.sleep(1)
        self.mirai.textToSpeech.say("do you have questions about your HVA ID ")
        while not (self.mirai.speechRecognition.recognizeWord()== 'yes' or self.mirai.speechRecognition.recognizeWord()== 'no'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'yes':
            self.mirai.textToSpeech.say("for this I refer you to the counter ")
            #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/pasje")
            time.sleep(3)
            self.q0()

        if self.mirai.speechRecognition.recognizeWord() == 'no':
            self.mirai.textToSpeech.say("then I don't know success either ")


    def q2(self):
        print ("ben bij vraag 2")
        time.sleep(1)
        self.mirai.textToSpeech.say("do you want to know where your classroom is?? ")

        while not (self.mirai.speechRecognition.recognizeWord() == 'yes' or self.mirai.speechRecognition.recognizeWord() == 'no'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'yes':
            self.mirai.textToSpeech.say("type your classroom number on the tablet ")
            #tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/lokaal zoeken.html")
            time.sleep(3)
            self.q0()

        if self.mirai.speechRecognition.recognizeWord() == 'no':
            self.q3()

    def q1(self):

        print ("ben bij vraag 1")
        time.sleep(1)
        self.mirai.textToSpeech.say("do you want to know where you are ")

        self.mirai.speechRecognition.recognizeWord()
        while not (self.mirai.speechRecognition.recognizeWord() == 'yes' or self.mirai.speechRecognition.recognizeWord() == 'no'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'yes':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat")
            #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/plattegrond.html")
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'no':
            self.q2()

    def askForHelp (self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        self.mirai.speechRecognition.setLanguage("Englishe")
        self.mirai.speechRecognition.startSpeecheRecognition()



        print ("ben bij vraag 0")
        self.mirai.textToSpeech.say("can I help you with something")


        while not (self.mirai.speechRecognition.recognizeWord() == 'yes' or self.mirai.speechRecognition.recognizeWord() == 'no'):
            time.sleep(1)

        if self.mirai.speechRecognition.recognizeWord() == 'yes':
            self.q1()

        if self.mirai.speechRecognition.recognizeWord() == 'no':
            self.mirai.textToSpeech.say("okey have a nice day")




    #tablet.reload()
    #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/hoofdpagina.html")
    #tablet.close_page()
    #askForHelp(session)






