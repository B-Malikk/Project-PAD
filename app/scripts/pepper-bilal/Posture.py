import qi
import argparse
import sys


def main(session):
    """
    PoseInit: Small example to make Nao go to an initial position.
    """
    # Get the services ALMotion & ALRobotPosture.

    motion_service = session.service("ALMotion")
    posture_service = session.service("ALRobotPosture")

    # Wake up robot
    motion_service.wakeUp()

    # Send robot to Stand Init
    posture_service.goToPosture("StandInit", 0.5)

    # Go to rest position
    motion_service.rest()

