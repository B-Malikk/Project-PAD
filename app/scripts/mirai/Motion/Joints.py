import math

class Joint(object):
    """
    Base class for a joint.
    A joint is part of a BodyPart.
    """

    def __init__(self, mirai, bodypart):
        self._bodypart = bodypart
        self._proxy = mirai.getProxy("ALMotion")

    def getName(self):
        name = ''
        try:
            name += self._bodypart.prefix
        except:
            pass

        name += self.__class__.__name__
        return name

class AngledJoint(Joint):
    """
    Base class for an angled joint, subclass of Joint.
    """

    _minAngle = 0 # Minimum angle (deg)
    _maxAngle = 180 # Maximum angle (deg)

    def setAngle(self, angle, fractionMaxSpeed=0.4):
        if angle > self._maxAngle or angle < self._minAngle:
            raise Exception("Angle {} is outside of range for joint {}. Minimum and maximum are {} and {} respectively."
                            .format(angle, self.getName(), self._minAngle, self._maxAngle))
        self._proxy.setAngles(self.getName(), math.radians(angle), fractionMaxSpeed)

    def setStiffness(self, stiffness):
        self._proxy.setStiffnesses([self.getName()], [stiffness])

    def getStiffness(self):
        return self._proxy.getStiffnesses([self.getName()])

class HeadYaw(AngledJoint):
    _minAngle = -119.5
    _maxAngle = 119.5

class HeadPitch(AngledJoint):
    _minAngle = -40.5
    _maxAngle = 25.5

class ShoulderPitch(AngledJoint):
    _minAngle = -119.5
    _maxAngle = 119.5

class ShoulderRoll(AngledJoint):
    _minAngle = 0.5
    _maxAngle = 89.5

class ElbowYaw(AngledJoint):
    _minAngle = -119.5
    _maxAngle = 119.5

class ElbowRoll(AngledJoint):
    _minAngle = -89.5
    _maxAngle = -0.5

class WristYaw(AngledJoint):
    _minAngle = -104.5
    _maxAngle = 104.5

class Hand(Joint):
    def open(self):
        self._proxy.openHand(self.getName())

    def close(self):
        self._proxy.closeHand(self.getName())

class HipRoll(AngledJoint):
    _minAngle = -29.5
    _maxAngle = 29.5

class HipPitch(AngledJoint):
    _minAngle = -59.5
    _maxAngle = 59.5

class KneePitch(AngledJoint):
    _minAngle = -29.5
    _maxAngle = 29.5
