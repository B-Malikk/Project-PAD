"""
A sample showing how to make a Python script as an app.
"""
from mirai._mirai import Mirai
import time
import threading
from mirai import Animations


if __name__ == "__main__":
    mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
    #mirai = Mirai("127.0.0.1", 2338, virtualRobot=True)


    mirai.motion.rest()

    mirai.engagementZone.setFirstLimit(0.5,90)
    mirai.engagementZone.setSecondLimit(1.5, 90)




