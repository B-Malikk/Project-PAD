import sys
import qi
from naoqi import ALProxy
from Animations import Animations
from Autonomy import AutonomousMovement
from Posture import Postures
from Motion import Motion
from TextToSpeech import TextToSpeech

class Mirai(object):

    def __init__(self, host, port, debug=False):
        self._session = qi.Session()
        self._host = host
        self._port = port
        try:
            self._session.connect("tcp://" + host + ":" + str(port))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + host + "\" on port " + str(port))
            sys.exit(1)

        if not debug:
            systemservice = self._session.service("ALSystem")
            print("Running NAOqi version " + systemservice.systemVersion())

        self.animations = Animations(self)
        self.autonomous = AutonomousMovement(self)
        self.posture = Postures(self)
        self.motion = Motion(self)
        self.textToSpeed = TextToSpeech(self)

    def getProxy(self, name):
        return ALProxy(name, self._host, self._port)