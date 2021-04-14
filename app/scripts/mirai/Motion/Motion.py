import math
from BodyParts import Head, LeftArm, RightArm, Knee

class Motion(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""

    def __init__(self, mirai):
        self.proxy = mirai.getProxy("ALMotion")
        self.head = Head(mirai)
        self.leftArm = LeftArm(mirai)
        self.rightArm = RightArm(mirai)
        self.knee = Knee(mirai)

    def wakeUp(self):
        self.proxy.wakeUp()

    def rest(self):
        self.proxy.rest()

    def setAngles(self, joints, angles, fractionMaxSpeed=.4):
        funcNames = []
        for joint in joints:
            funcNames.append(joint.getName())

        funcAngles = []
        for angle in angles:
            funcAngles.append(math.radians(angle))
        self.proxy.setAngles(funcNames, funcAngles, fractionMaxSpeed)
