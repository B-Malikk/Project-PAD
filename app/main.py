"""
A sample showing how to make a Python script as an app.
"""
import threading
import time
import random

from mirai._mirai import Mirai
from mirai.MQTT import MQTTListenerBaseClass
from datetime import datetime


class Main(MQTTListenerBaseClass):
    topic = 'Mirai/#'
    lastMessage = {}
    lastAction = {}

    messages = []

    def __init__(self, mirai):
        super(Main, self).__init__(mirai)

        #Motion/speech
        self.mirai.textToSpeech.sayAnimated("kaas", mode='random')
        self.mirai.motion.wakeUp()  # awake robot
        self.mirai.posture.StandInit.apply()
        #self.mirai.motion.hoofd()
        self.mirai.textToSpeech.setVolume(0.7)

        #Awareness/Perception
        self.mirai.basicAwareness.setBA(False)  # basic awareness on specialy human tracking
        self.mirai.basicAwareness.setEnagement("SemiEngaged") # sret sensitifitie mode for people who engage the robot
        self.mirai.peoplePerception.setDisappearTime(5) # Set time for how long a person disappears from the PeopleList if he/she is no more visible.

        #Speechrecognition
        vocabulary=['ja','nee','help mij','ik ben mijn pasje kwijt','Ik weet niet waar mijn lokaal is', 'Ik heb hulp nodig', 'Hoe gaat het?']
        self.mirai.speechRecognition.setLanguage("Dutch")
        self.mirai.speechRecognition.setVocabulary(vocabulary)

        #Enagementzone
        self.mirai.engagementZone.setFirstLimit(0.7, 90)
        self.mirai.engagementZone.setSecondLimit(1.2,90)
        self.mirai.engagementZone.start()

        #Tablet
        self.mirai.tablet.closePage()
        self.mirai.tablet.reload()
        time.sleep(5)
        self.mirai.tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/language.html")
        #self.mirai.tablet.openPage("https://www.google.nl")

        thread = threading.Thread(target=self.processMessages)
        thread.start()

    def on_message(self, client, userdata, msg):
        if self.mirai.robotState.getPosture() == 'open':
            self.messages.append(msg)

    def processMessages(self):
        while True:
            if len(self.messages) > 0:
                msg = self.messages[0]
                self.messages.pop(0)
                self.handleMessage(msg)

    def handleMessage(self, msg):
        topic = msg.topic
        print(topic)
        self.lastMessage.update({topic: datetime.utcnow()})

        if topic == 'Mirai/CardReader/success' or topic == 'Mirai/CardReader/error':
            self.updateAction(topic)
            self.mirai.textToSpeech.sayAnimated("Welkom", mode= 'random')

        elif topic == 'Mirai/PeoplePerception/noPeople':
            #self.mirai.motion.wakeUp()  # awake robot
            self.mirai.motion.hoofd()
            self.mirai.posture.StandInit.apply()

        elif topic == 'Mirai/PeoplePerception/tooClose':
            if self.timeSinceAction(topic) > 7:
                self.mirai.textToSpeech.sayAnimated("Denken jullie om de anderhalve meter?", mode= 'random')
                self.updateAction(topic)

        elif topic == 'Mirai/EngagementZone/enteredZone2'and self.mirai.robotState.getPosture() == 'open':
            if self.timeSinceAction(topic) > 15:
                #self.mirai.basicAwareness.pausAwareness()
                self.mirai.robotState.setPosture('scan')
                self.updateAction(topic)
                self.mirai.textToSpeech.sayAnimated("vergeet niet je pasje te scannen", mode= 'contextual')
                time.sleep(3)

                self.mirai.robotState.setPosture('open')
                #self.mirai.basicAwareness.resumeAwareness()

        elif topic == 'Mirai/EngagementZone/enteredZone1' and self.mirai.robotState.getPosture() == 'open':
            if self.timeSinceAction(topic) > 15:
                #self.mirai.basicAwareness.pausAwareness()
                self.mirai.robotState.setPosture('help')
                #vocabulary = ['ja', 'nee', 'hallo', 'brood', 'boom', 'appelflap', 'deur', 'ssht', 'remoer']
                self.mirai.speechRecognition.setLanguage("Dutch")
                #self.mirai.speechRecognition.setVocabulary(vocabulary)
                self.mirai.textToSpeech.sayAnimated("kan ik je ergens mee helpen", mode= 'random')
                self.mirai.textToSpeech.sayAnimated("selecteer een taal op het taplet", mode= 'random')
                # self.mirai.speechRecognition.startSpeecheRecognition()
                # try:
                #     self.mirai.speechRecognition.cleareMemory()
                # except:
                #     pass
                #
                # while not (self.mirai.speechRecognition._word == 'ja' or self.mirai.speechRecognition._word == 'nee'):
                #     print "while not"
                #
                # if self.mirai.speechRecognition._word == 'ja':
                #         self.mirai.speechRecognition.stop()
                #         self.mirai.textToSpeech.sayAnimated("selecteer een taal op het taplet")
                #         self.mirai.robotState.setPosture('tablet')
                #         self.mirai.basicAwareness.resumeAwareness()
                #
                # if self.mirai.speechRecognition._word == 'nee':
                #         self.mirai.speechRecognition.stop()
                #         self.mirai.textToSpeech.sayAnimated("fijne dag nog")
                #         time.sleep(1)
                #         self.mirai.robotState.setPosture('open')
                #         self.mirai.basicAwareness.resumeAwareness()
                self.updateAction(topic)
                time.sleep(3)
                self.mirai.robotState.setPosture('open')
                #self.mirai.basicAwareness.resumeAwareness()

        elif topic == 'Mirai/PeoplePerception/personArrived' and self.mirai.robotState.getPosture()=='open':
            if self.timeSinceAction(topic) > 15:
                #self.mirai.basicAwareness.pausAwareness()
                self.mirai.robotState.setPosture('welcome')
                listGestures=["hallo ", "goedemiddag","salaam","nihhaauu","merhabaa"]
                groet=random.choice(listGestures)
                self.mirai.animations.Hey.run()
                self.mirai.textToSpeech.say(groet)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")
                time.sleep(3)
                #self.mirai.basicAwareness.resumeAwareness()
                self.mirai.robotState.setPosture('open')
                self.updateAction(topic)

    def updateAction(self, topic):
        self.lastAction.update({topic: datetime.utcnow()})

    def timeSinceAction(self, topic):
        try:
            timesince = self.lastAction[topic]
        except:
            return 99999
        time = (datetime.utcnow() - self.lastAction[topic]).seconds
        print(time)
        return time

if __name__ == "__main__":
    mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
    main = Main(mirai)






