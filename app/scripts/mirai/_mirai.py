import sys
import qi
from naoqi import ALProxy
from Animations import Animations
from Autonomy import AutonomousMovement
from Posture import Postures
from Motion import Motion

class Mirai(object):

    def __init__(self, host, port, debug=False):
        self.session = qi.Session()
        self.host = host
        self.port = port
        try:
            self.session.connect("tcp://" + host + ":" + str(port))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + host + "\" on port " + str(port))
            sys.exit(1)

        if not debug:
            systemservice = self.session.service("ALSystem")
            print("Running NAOqi version " + systemservice.systemVersion())

        self.animations = Animations(self)
        self.autonomous = AutonomousMovement(self)
        self.posture = Postures(self)
        self.motion = Motion(self)

    def getProxy(self, name):
        return ALProxy(name, self.host, self.port)