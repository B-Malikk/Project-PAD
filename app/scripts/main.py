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
    running = False

    def __init__(self, mirai):
        super(Main, self).__init__(mirai)
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

    def on_event(self, msg):
        topic = msg.topic
        print(topic)
        self.lastMessage.update({topic: datetime.utcnow()})

        if topic == 'Mirai/CardReader/success':
            self.mirai.textToSpeech.say("Welkom")
            self.updateAction(topic)

        elif topic == 'Mirai/PeoplePerception/tooClose':
            if self.timeSinceAction(topic) > 10:
                self.mirai.textToSpeech.say("Denken jullie om de anderhalve meter?")
                self.updateAction(topic)

        elif topic == 'Mirai/EngagementZone/enteredZone2':
            if self.timeSinceAction(topic) > 10:
                print ("wil je pasje scannen")
                self.mirai.robotState.setPosture('scan')
                self.mirai.textToSpeech.say("Scan je pasje")
                self.mirai.robotState.setPosture('open')
                self.updateAction(topic)

        elif topic == 'Mirai/EngagementZone/enteredZone1':
            if self.timeSinceAction(topic) > 10:
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
                        self.mirai.robotState.setPosture('open')

                if self.mirai.speechRecognition.recognizeWord() == 'nee':
                        self.mirai.speechRecognition.stop()
                        self.mirai.textToSpeech.say("fijne dag nog")
                        self.mirai.robotState.setPosture('open')
                self.updateAction(topic)
        elif topic == 'Mirai/PeoplePerception/personArrived':
            if self.timeSinceAction(topic) > 10:
                listGestures=["hallo ", "goedemiddag","salaam","nihhaauu","merhabaa"]
                groet=random.choice(listGestures)
                self.mirai.robotState.setPosture('welcome')
                self.mirai.animations.Hey.run(1)
                self.mirai.textToSpeech.say(groet)
                self.mirai.textToSpeech.say("Welkom in het Wibauthuis")
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






