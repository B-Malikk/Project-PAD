import math
import threading
from Chains import Head, LArm, RArm, Leg

class Motion(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""


    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALMotion")
        self._tts = mirai.getProxy("ALTextToSpeech")
        self.head = Head(mirai)
        self.leftArm = LArm(mirai)
        self.rightArm = RArm(mirai)
        self.leg = Leg(mirai)

    def wakeUp(self):
        self._proxy.wakeUp()

    def rest(self):
        self._proxy.rest()

    def enableArmsMove(self):
        self._proxy.setMoveArmsEnabled(True, True)

    def disableArmsMove(self):
        self._proxy.setMoveArmsEnabled(False, False)

    def moveForward(self, meters):
        self._proxy.moveTo(meters, 0, 0)

    def moveLeft(self, meters):
        self._proxy.moveTo(0, meters, 0)

    def moveRight(self, meters):
        self._proxy.moveTo(0, -meters, 0)

    def moveBack(self, meters):
        self._proxy.moveTo(-meters, 0, 0)

    def moveTo(self, x, y, degrees):
        self._proxy.moveTo(x, y, math.radians(degrees))

    def moveToward(self, velocityX, velocityY, velocityAxis):
        # x: +1 and -1 are forward and backward
        # y: +1 and -1 are left and right
        # axis: +1 and -1 are anticlockwise and clockwise
        self._proxy.moveToward(velocityX, velocityY, velocityAxis)

    def rotateAntiClockWise(self, degrees):
        self._proxy.moveTo(0, 0, math.radians(degrees))

    def rotateClockWise(self, degrees):
        self._proxy.moveTo(0, 0, math.radians(degrees))

    def stopMove(self):
        self._proxy.stopMove()

    def setAngles(self, joints, angles, fractionMaxSpeed=.4):
        funcNames = []
        for joint in joints:
            if isinstance(joint, str):
                funcNames.append(joint)
            else:
                funcNames.append(joint.getName())

        funcAngles = []
        for angle in angles:
            funcAngles.append(math.radians(angle))
        self._proxy.setAngles(funcNames, funcAngles, fractionMaxSpeed)

    def setStiffnesses(self, joints, stiffnesses):
        funcNames = []
        for joint in joints:
            if isinstance(joint, str):
                funcNames.append(joint)
            else:
                funcNames.append(joint.getName())

        self._proxy.setStiffnesses(funcNames, stiffnesses)


    def enableIdle(self):
        self._proxy.setIdlePostureEnabled('Body', True)

    def disableIdle(self):
        self._proxy.setIdlePostureEnabled('Body', False)

    def point(self):
        names = ["LShoulderRoll", "LShoulderPitch", "LElbowRoll", "LWristYaw"]
        angleLists = [3, 3, -0.0087, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def scanner(self):
        names = ["RShoulderRoll", "RShoulderPitch", "RElbowRoll", "RWristYaw"]
        angleLists = [3, 3, -0.0087, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def scan2(self):
        names = ["RShoulderRoll", "RWristYaw"]
        angleLists = [1.5, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def hoofd(self):
        self._proxy.angleInterpolation("HeadPitch", -0.2, 2, True)
