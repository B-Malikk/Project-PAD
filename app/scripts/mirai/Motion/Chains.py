from BodyParts import Hip, Knee, Shoulder, Elbow, Wrist
from Joints import HeadYaw, HeadPitch, Hand


class Chain(object):
    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALMotion")

    def setStiffness(self, stiffness):
        self._proxy.setStiffnesses(self.__class__.__name__, stiffness)

    def getStiffness(self):
        return self._proxy.getStiffnesses(self.__class__.__name__)

class Arm(Chain):
    """
    Base class for an arm. Prefix should be set by subclass.
    """
    _prefix = '' #L or R

    def __init__(self, mirai):
        super(Arm, self).__init__(mirai)
        self.shoulder = Shoulder(mirai, self)
        self.elbow = Elbow(mirai, self)
        self.wrist = Wrist(mirai, self)
        self.hand = Hand(mirai, self) # Hand is a Joint, so should get passed this object directly

class LArm(Arm):
    _prefix = 'L'

class RArm(Arm):
    _prefix = 'R'

class Leg(Chain):
    def __init__(self, mirai):
        super(Leg, self).__init__(mirai)
        self.hip = Hip(mirai)
        self.knee = Knee(mirai)

class Head(Chain):
    def __init__(self, mirai):
        super(Head, self).__init__(mirai)
        self.yaw = HeadYaw(mirai, self)
        self.pitch = HeadPitch(mirai, self)