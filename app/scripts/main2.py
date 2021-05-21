import threading

from mirai._mirai import Mirai
import time



class Main(object):
    def __init__(self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        self.mirai.motion.wakeUp()
        vocabulary=['ja','nee']
        self.mirai.textToSpeech.say("kaas")
        self.mirai.speechRecognition.setLanguage("Dutch")
        self.mirai.speechRecognition.setVocabulary(vocabulary)

        self.mirai.engagementZone.setFirstLimit(1, 90)
        self.mirai.engagementZone.setSecondLimit(1.8,90)
        self.mirai.engagementZone.start()
        thread1 = threading.Thread(target=self.sayScanCard)
        thread1.start()



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
                        self.mirai.robotState.setPosture('open')


                if self.mirai.speechRecognition.recognizeWord() == 'nee':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.say("fijne dag nog")
                        self.mirai.robotState.setPosture('open')



if __name__ == "__main__":
    main = Main()
