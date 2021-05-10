"""
A sample showing how to make a Python script as an app.
"""
from mirai._mirai import Mirai


class Main(object):
    def __init__(self):
        self.mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
        self.mirai.motion.rest()
        self.mirai.engagementZone.setFirstLimit(0.5,90)
        self.mirai.engagementZone.setSecondLimit(1.5, 90)

    def sayScanCard(self):
        previous = self.mirai.engagementZone.personInZone1
        while True:
            if self.mirai.engagementZone.personInZone1 == True and previous == False:
                pass
                # Scan card motion - this is for Bryan
                self.mirai.textToSpeech.say("Scan je pasje")
            previous = self.mirai.engagementZone.personInZone1

    def sayWelcome(self):
        previous = self.mirai.peoplePerception._peopleCounter
        while True:
            if self.mirai.peoplePerception._peopleCounter == 1 and previous == 0:
                self.mirai.animations.Hey.run(1)
                self.mirai.textToSpeech.say("Welcom in het Wibauthuis")
            previous = self.mirai.peoplePerception._peopleCounter

if __name__ == "__main__":
    main = Main()






