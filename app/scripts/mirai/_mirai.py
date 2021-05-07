
import qi
import sys
from naoqi import ALProxy
#from Animations import Animations
#from Autonomy import AutonomousMovement
#from Posture import Postures
#from Motion import Motion
#from TextToSpeech import TextToSpeech
#from SpeechRecognition import SpeechRecognition
#from MQTT import MQTTListener
from mirai.Animations import Animations
from mirai.Autonomy import AutonomousMovement
from mirai.Motion.Motion import Motion
from mirai.Posture import Postures
from mirai.SpeechRecognition import SpeechRecognition
from mirai.TextToSpeech import TextToSpeech
from mirai.Dialog import Dialog
from mirai.Tablet import Tablet
from mirai.PeoplePerception.EngagementZone import EngagementZones
from mirai.PeoplePerception.FaceDetection import FaceDetection
from mirai.PeoplePerception.PeoplePerception import PeoplePerception



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
        self.tablet = Tablet(self)
        self.peoplePerception = PeoplePerception(self)
        #self.mqtt = MQTTListener(self)

    def getProxy(self, name):
        try:
            proxy = ALProxy(name, self._host, self._port)
            return proxy
        except:
            msg = "Service {} can't be found.".format(name)
            if self._virtualRobot:
                msg += " It may not be available on a virtual robot."

            raise Exception(msg)