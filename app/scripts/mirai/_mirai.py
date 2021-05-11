
import qi
import sys
from naoqi import ALProxy

from Animations import Animations
from Autonomy import AutonomousMovement
from Motion.Motion import Motion
from Posture import Postures
from SpeechRecognition import SpeechRecognition
from TextToSpeech import TextToSpeech
from Dialog import Dialog
from Tablet import Tablet
from PeoplePerception.EngagementZone import EngagementZones
from PeoplePerception.FaceDetection import FaceDetection
from PeoplePerception.PeoplePerception import PeoplePerception
from MQTTCardReader import MQTTCardReader
from MQTTWebListener import MQTTWebListener
from progamNL import dutchProgram
from progamENG import engProgram


class Mirai(object):

    def __init__(self, host, port, virtualRobot=False):
        self._session = qi.Session()
        self._host = host
        self._port = port
        self._virtualRobot = virtualRobot
        try:
            self._session.connect("tcp://" + host + ":" + str(port))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + host + "\" on port " + str(port))
            sys.exit(1)

        if not virtualRobot:
            # Things that can only be run on a real robot
            systemservice = self._session.service("ALSystem")
            print("Running NAOqi version " + systemservice.systemVersion())
            self.speechRecognition = SpeechRecognition(self)


        self.animations = Animations(self)
        self.autonomous = AutonomousMovement(self)
        self.posture = Postures(self)
        self.motion = Motion(self)
        self.textToSpeech = TextToSpeech(self)
        self.dialog = Dialog(self)
        self.engagementZone = EngagementZones(self)
        self.faceDetection = FaceDetection(self)
        self.peoplePerception = PeoplePerception(self)
        self.mqttCardReader = MQTTCardReader(self)
        self.mqttWebListener = MQTTWebListener(self)
        self.tablet = Tablet(self)
        self.program1=dutchProgram(self)
        self.program2 = dutchProgram(self)

    def getProxy(self, name):
        try:
            return self._session.service(name)
        except:
            pass
        try:
            proxy = ALProxy(name, self._host, self._port)
            return proxy
        except:
            msg = "Service {} can't be found.".format(name)
            if self._virtualRobot:
                msg += " It may not be available on a virtual robot."

            raise Exception(msg)