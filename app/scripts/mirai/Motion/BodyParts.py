from Joints import *

class Shoulder(object):
    def __init__(self, mirai, bodypart):
        self._prefix = bodypart._prefix
        self.pitch = ShoulderPitch(mirai, self)
        self.roll = ShoulderRoll(mirai, self)

class Elbow(object):
    def __init__(self, mirai, bodypart):
        self._prefix = bodypart._prefix
        self.yaw = ElbowYaw(mirai, self)
        self.roll = ElbowRoll(mirai, self)

class Wrist(object):
    def __init__(self, mirai, bodypart):
        self._prefix = bodypart._prefix
        self.yaw = WristYaw(mirai, self)

class Hip(object):
    def __init__(self, mirai):
        self.roll = HipRoll(mirai, self)
        self.pitch = HipPitch(mirai, self)

class Knee(object):
    def __init__(self, mirai):
        self.pitch = KneePitch(mirai, self)
