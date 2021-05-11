import qi
import time
import sys
import argparse
from naoqi import ALProxy

joint = ALProxy("ALMotion", "mirai.robot.hva-robots.nl", 9559)
tts = ALProxy("ALTextToSpeech", "mirai.robot.hva-robots.nl", 9559)
posture_service = ALProxy("ALRobotPosture", "mirai.robot.hva-robots.nl", 9559)
tts.setLanguage("Dutch")


def point():
    # Steekt arm naar voren om pasje te scannen
    names = ["LShoulderRoll", "LShoulderPitch"]
    joint.setStiffnesses(names, 1)
    angleLists = [2, 2]
    times = [2, 2]
    isAbsolute = True
    joint.angleInterpolation(names, angleLists, times, isAbsolute)


posture_service.goToPosture("StandInit", 0.7)
point()


