"""
A sample showing how to make a Python script as an app.
"""
import threading
import time
import random

from mirai._mirai import Mirai


class Main(object):
    def __init__(self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        self.mirai.motion.wakeUp()
        self.mirai.motion.hoofd()
        vocabulary=['ja','nee']
        self.mirai.textToSpeech.say("kaas")
        self.mirai.speechRecognition.setLanguage("Dutch")
        self.mirai.speechRecognition.setVocabulary(vocabulary)

        self.mirai.engagementZone.setFirstLimit(0.7, 90)
        self.mirai.engagementZone.setSecondLimit(1.5,90)
        self.mirai.engagementZone.start()

        self.mirai.tablet.closePage()
        self.mirai.tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/language.html")
        #self.mirai.tablet.openPage("https://www.google.nl")

        thread1 = threading.Thread(target=self.sayScanCard)
        thread2 = threading.Thread(target=self.sayWelcome)
        thread1.start()
        thread2.start()

    def sayScanCard(self):
        while True:

            if self.mirai.engagementZone._personEnteredZone2 and self.mirai.robotState.getPosture()== 'open':
                print ("wil je pasje scannen")
                self.mirai.robotState.setPosture('scan')
                self.mirai.textToSpeech.say("Scan je pasje")
                self.mirai.robotState.setPosture('open')
                time.sleep(2)

            if self.mirai.engagementZone._personEnteredZone1 and self.mirai.robotState.getPosture()== 'open':
                self.mirai.robotState.setPosture('help')
                self.mirai.textToSpeech.say("kan ik je ergens mee helpen")
                self.mirai.speechRecognition.startSpeecheRecognition()

                while not (self.mirai.speechRecognition.recognizeWord() == 'ja' or self.mirai.speechRecognition.recognizeWord() == 'nee'):
                    time.sleep(1)
                print "uit while not"

                if self.mirai.speechRecognition.recognizeWord() == 'ja':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.say("selecteer een taal op de tablet")
                        self.mirai.robotState.setPosture('tablet')
                        time.sleep(20)
                        self.mirai.robotState.setPosture('open')



                if self.mirai.speechRecognition.recognizeWord() == 'nee':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.say("fijne dag nog")
                        time.sleep(10)
                        self.mirai.robotState.setPosture('open')

    def sayWelcome(self):
        while True:
            if self.mirai.peoplePerception._newPersonDetected == True and self.mirai.robotState.getPosture()=='open':
                print ("welkom")
                listGestures=["hallo ", "goedemiddag","salaam","nihhaauu","merhabaa"]
                groet=random.choice(listGestures)
                self.mirai.robotState.setPosture('welcome')
                self.mirai.animations.Hey.run(1)
                self.mirai.textToSpeech.say(groet)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")
                time.sleep(2)
                self.mirai.robotState.setPosture('open')
                time.sleep(15)




if __name__ == "__main__":
    main = Main()






