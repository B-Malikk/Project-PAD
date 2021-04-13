import sys
import qi
import Animations
from Autonomy import AutonomousMovement

class Mirai(object):

    def __init__(self, host, ip):
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + host + ":" + str(ip))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + host + "\" on port " + str(ip))
            sys.exit(1)

        systemservice = self.session.service("ALSystem")
        print("Running NAOqi version " + systemservice.systemVersion())

        self.animations = Animations.get_all(self.session)
        self.autonomousMovement = AutonomousMovement(self.session)