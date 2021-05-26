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
        thread = threading.Thread(target=self.processMessages)
        thread.start()

        #Motion/speech
        self.mirai.motion.wakeUp()  # awake robot
        self.mirai.posture.StandInit.apply()
        self.mirai.motion.hoofd()
        self.mirai.textToSpeech.setVolume(0.3)
        self.mirai.textToSpeech.sayAnimated("kaas", mode='random')

        #Awareness/Perception
        self.mirai.basicAwareness.setBA(False)  # basic awareness on specialy human tracking
        #self.mirai.basicAwareness.setEnagement("SemiEngaged") # sret sensitifitie mode for people who engage the robot
        self.mirai.peoplePerception.setDisappearTime(15) # Set time for how long a person disappears from the PeopleList if he/she is no more visible.

        #Speechrecognition
        vocabulary=['ja','nee','haloo','ssttt','remoer','aardappel','flesje','boom']
        self.mirai.speechRecognition.setLanguage("Dutch")
        self.mirai.speechRecognition.setVocabulary(vocabulary)

        #Enagementzone
        self.mirai.engagementZone.setFirstLimit(0.7, 90)
        self.mirai.engagementZone.setSecondLimit(1.2,90)
        self.mirai.engagementZone.start()

        #Tablet
        self.mirai.tablet.closePage()
        self.mirai.tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/language.html")
        #self.mirai.tablet.openPage("https://www.google.nl")

    def on_message(self, client, userdata, msg):
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

        if topic == 'Mirai/CardReader/success':
            self.updateAction(topic)
            self.mirai.textToSpeech.sayAnimated("Welkom", mode= 'random')

        elif topic == 'Mirai/PeoplePerception/tooClose':
            if self.timeSinceAction(topic) > 10:
                self.mirai.textToSpeech.sayAnimated("Denken jullie om de anderhalve meter?", mode= 'random')
                self.updateAction(topic)

        elif topic == 'Mirai/EngagementZone/enteredZone2'and self.mirai.robotState.getPosture() == 'open':
            if self.timeSinceAction(topic) > 10:
                print ("wil je pasje scannen")
                self.updateAction(topic)
                self.mirai.robotState.setPosture('scan')
                self.mirai.textToSpeech.sayAnimated("Scan je pasje", mode= 'random')
                time.sleep(2)
                self.mirai.robotState.setPosture('open')

        elif topic == 'Mirai/EngagementZone/enteredZone1' and self.mirai.robotState.getPosture() == 'open':
            if self.timeSinceAction(topic) > 10:
                self.mirai.robotState.setPosture('help')
                self.mirai.textToSpeech.sayAnimated("kan ik je ergens mee helpen", mode= 'random')
                #self.mirai.textToSpeech.sayAnimated("selecteer een probleem op het taplet", mode= 'random')
                self.mirai.speechRecognition.startSpeecheRecognition()
                try:
                    self.mirai.speechRecognition.cleareMemory()
                except:
                    pass

                while not (self.mirai.speechRecognition._word == 'ja' or self.mirai.speechRecognition._word == 'nee'):
                    print "while not"

                if self.mirai.speechRecognition._word == 'ja':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.sayAnimated("selecteer een taal op het taplet")
                        self.mirai.robotState.setPosture('tablet')
                        self.mirai.basicAwareness.resumeAwareness()

                if self.mirai.speechRecognition._word == 'nee':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.sayAnimated("fijne dag nog")
                        time.sleep(1)
                        self.mirai.robotState.setPosture('open')
                        self.mirai.basicAwareness.resumeAwareness()
                self.updateAction(topic)

        elif topic == 'Mirai/PeoplePerception/personArrived' and self.mirai.robotState.getPosture()=='open':
            if self.timeSinceAction(topic) > 10:
                self.mirai.basicAwareness.pausAwareness()
                listGestures=["hallo ", "goedemiddag","salaam","nihhaauu","merhabaa"]
                groet=random.choice(listGestures)
                self.updateAction(topic)
                self.mirai.robotState.setPosture('welcome')
                self.mirai.animations.Hey.run()
                self.mirai.textToSpeech.say(groet)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")
                time.sleep(2)
                self.mirai.robotState.setPosture('open')
                self.mirai.basicAwareness.resumeAwareness()

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






