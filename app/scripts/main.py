"""
A sample showing how to make a Python script as an app.
"""
from mirai import Mirai
from mirai import Animations


if __name__ == "__main__":
    #mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
    mirai = Mirai("127.0.0.1", 50194, virtualRobot=True)