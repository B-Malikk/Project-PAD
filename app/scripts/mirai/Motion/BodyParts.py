from Joints import *

class BodyPart(object):
    def __init__(self, mirai):
        self.mirai = mirai

class Head(BodyPart):
    def __init__(self, mirai):
        super(Head, self).__init__(mirai)
        self.headYaw = HeadYaw(mirai, self)
        self.headPitch = HeadPitch(mirai, self)

class Arm(BodyPart):
    """
    Base class for an arm. Prefix should be set by subclass.
    """
    prefix = '' #L or R

    def __init__(self, mirai):
        super(Arm, self).__init__(mirai)
        self.shoulderPitch = ShoulderPitch(mirai, self)
        self.shoulderRoll = ShoulderRoll(mirai, self)
        self.elbowJaw = ElbowJaw(mirai, self)
        self.elbowRoll = ElbowRoll(mirai, self)
        self.wristYaw = WristYaw(mirai, self)
        self.hand = Hand(mirai, self)

class LeftArm(Arm):
    prefix = 'L'

class RightArm(Arm):
    prefix = 'R'

class Hip(BodyPart):
    def __init__(self, mirai):
        super(Hip, self).__init__(mirai)
        self.hipRoll = HipRoll(mirai, self)
        self.hipPitch = HipPitch(mirai, self)

class Knee(BodyPart):
    def __init__(self, mirai):
        super(Knee, self).__init__(mirai)
        self.kneePitch = KneePitch(mirai, self)