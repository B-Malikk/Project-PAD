"""
A sample showing how to make a Python script as an app.
"""
import threading
import time

from mirai._mirai import Mirai


class Main(object):
    def __init__(self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        #self.mirai.motion.wakeUp()
        self.mirai.motion.hoofd()
        self.mirai.peoplePerception.setRange(4)
        self.mirai.peoplePerception.setDisappearTime(10)


        self.mirai.textToSpeech.say("kaas")
        self.mirai.tablet.closePage()
        self.mirai.tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/language.html")

        thread1 = threading.Thread(target=self.sayScanCard)
        thread2 = threading.Thread(target=self.sayWelcome)
        thread1.start()
        thread2.start()

    def sayScanCard(self):
        while True:
            if self.mirai.peoplePerception.getNewPersonDistance() <= 1 and self.mirai.peoplePerception.getNewPersonDistance() >= 0.8 and self.mirai.posture.getPosture()=='open':
                self.mirai.posture.setPosture('scan')
                self.mirai.motion.scanner()
                self.mirai.textToSpeech.say("Scan je pasje")
                self.mirai.posture.setPosture('open')
                time.sleep(20)

    def sayWelcome(self):
        while True:
            if self.mirai.peoplePerception.newPersonDetected and self.mirai.posture.getPosture()=='open':
                self.mirai.posture.setPosture('welcome')
                self.mirai.animations.Hey.run(1)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")
                self.mirai.posture.setPosture('open')
                time.sleep(20)

if __name__ == "__main__":
    main = Main()






