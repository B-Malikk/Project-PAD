# Dit programma wordt gebruikt om de rechter arm met de scanner omhoog te brengen voor scannen.

import qi
import time
import sys
import argparse

from naoqi import ALProxy


joint = ALProxy("ALMotion", "mirai.robot.hva-robots.nl",9559 )
tts = ALProxy("ALTextToSpeech", "mirai.robot.hva-robots.nl",9559)
posture_service = ALProxy("ALRobotPosture", "mirai.robot.hva-robots.nl",9559)
tts.setLanguage("Dutch")


def grip():
    names = ["RHand"]
    joint.setStiffnesses(names, 0.5)
    angleLists = [0, 1]
    times = [2, 10]
    isAbsolute = True
    joint.angleInterpolation(names, angleLists, times, isAbsolute)

def arm():
    #Steekt arm naar voren om pasje te scannen
    names = ["RElbowRoll", "RShoulderPitch", "RWristYaw"]
    joint.setStiffnesses(names, 0.5)
    angleLists = [1, 0.785398, 2]
    times = [2, 2, 2]
    isAbsolute = True
    joint.angleInterpolation(names, angleLists, times, isAbsolute)



arm()
grip()
posture_service.goToPosture("StandInit", 0.7)