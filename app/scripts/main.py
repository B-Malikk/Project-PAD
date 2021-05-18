"""
A sample showing how to make a Python script as an app.
"""
import threading

from mirai._mirai import Mirai


class Main(object):
    def __init__(self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        self.mirai.motion.wakeUp()
        self.mirai.engagementZone.setFirstLimit(1,90)
        print(self.mirai.engagementZone.getFirstLimit())

        self.mirai.textToSpeech.say("kaas")
        self.mirai.tablet.closePage()
        #self.mirai.tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/language.html")

        thread = threading.Thread(target=self.mirai.peoplePerception.startPeopleDetection(5,8))
        thread1 = threading.Thread(target=self.sayScanCard)
        thread2 = threading.Thread(target=self.sayWelcome)
        thread.start()
        thread1.start()
        thread2.start()

    def sayScanCard(self):
        while True:
            personInzone1 = self.mirai.engagementZone.personInZone1
            if personInzone1:
                # Scan card motion - this is for Bryan
                self.mirai.textToSpeech.say("Scan je pasje")

    def sayWelcome(self):
        previous = self.mirai.peoplePerception._peopleCounter
        while True:
            if self.mirai.peoplePerception._peopleCounter == 1 and previous == 0:
                self.mirai.animations.Hey.run(1)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")

if __name__ == "__main__":

    main = Main()






