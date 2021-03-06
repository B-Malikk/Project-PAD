import math
import threading

class Motion(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""


    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALMotion")
        self._tts = mirai.getProxy("ALTextToSpeech")

    def wakeUp(self):
        self._proxy.wakeUp()

    def rest(self):
        self._proxy.rest()

    def enableArmsMove(self):
        self._proxy.setMoveArmsEnabled(True, True)

    def disableArmsMove(self):
        self._proxy.setMoveArmsEnabled(False, False)

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

    def point(self): #Points to service desk
        names = ["LShoulderRoll", "LShoulderPitch", "LElbowRoll", "LWristYaw"]
        angleLists = [3, 3, -0.0087, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def scanner(self): #Adresses the scanner
        names = ["RShoulderRoll", "RShoulderPitch", "RElbowRoll", "RWristYaw"]
        angleLists = [3, 3, -0.0087, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def scan2(self): #Adresses the scanner
        names = ["RShoulderRoll", "RWristYaw"]
        angleLists = [1.5, -1.8329]
        times = [1, 1, 2, 2]
        isAbsolute = True
        self._proxy.angleInterpolation(names, angleLists, times, isAbsolute)

    def hoofd(self): #Tilts the head up a bit
        self._proxy.angleInterpolation("HeadPitch", -0.2, 2, True)
