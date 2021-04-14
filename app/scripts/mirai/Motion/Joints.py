import math

class Joint(object):
    """
    Base class for a joint.
    A joint is part of a BodyPart.
    """

    def __init__(self, mirai, bodypart):
        self.mirai = mirai
        self.bodypart = bodypart
        self.proxy = self.mirai.getProxy("ALMotion")

    def getName(self):
        name = ''
        try:
            name += self.bodypart.prefix
        except:
            pass

        name += self.__class__.__name__
        return name

class AngledJoint(Joint):
    """
    Base class for an angled joint, subclass of Joint.
    """

    minAngle = 0 # Minimum angle (deg)
    maxAngle = 180 # Maximum angle (deg)

    def setAngle(self, angle, fractionMaxSpeed=0.4):
        if angle > self.maxAngle or angle < self.minAngle:
            raise Exception("Angle {} is outside of range for joint {}. Minimum and maximum are {} and {} respectively."
                            .format(angle, self.getName(), self.minAngle, self.maxAngle))

        self.proxy.setAngles([self.getName()], [math.radians(angle)], fractionMaxSpeed)

class HeadYaw(AngledJoint):
    minAngle = -119.5
    maxAngle = 119.5

class HeadPitch(AngledJoint):
    minAngle = -40.5
    maxAngle = 25.5

class ShoulderPitch(AngledJoint):
    minAngle = -119.5
    maxAngle = 119.5

class ShoulderRoll(AngledJoint):
    minAngle = 0.5
    maxAngle = 89.5

class ElbowJaw(AngledJoint):
    minAngle = -119.5
    maxAngle = 119.5

class ElbowRoll(AngledJoint):
    minAngle = -89.5
    maxAngle = -0.5

class WristYaw(AngledJoint):
    minAngle = -104.5
    maxAngle = 104.5

class Hand(Joint):
    def open(self):
        self.proxy.openHand(self.getName())

    def close(self):
        self.proxy.closeHand(self.getName())

class HipRoll(AngledJoint):
    minAngle = -29.5
    maxAngle = 29.5

class HipPitch(AngledJoint):
    minAngle = -59.5
    maxAngle = 59.5

class KneePitch(AngledJoint):
    minAngle = -29.5
    maxAngle = 29.5
