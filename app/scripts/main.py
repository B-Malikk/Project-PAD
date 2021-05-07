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


    #mirai.motion.wakeUp()
    mirai.tablet.openPage("https://res.cloudinary.com/practicaldev/image/fetch/s--IoJSEQo3--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lx73zhig4biqogekj1jl.png")
    mirai.textToSpeech.say("testttt")


    mirai.engagementZone.setFirstLimit(0.5,90)
    mirai.engagementZone.setSecondLimit(1.5, 90)

    threading.Thread(target=mirai.peoplePerception.startPeopleDetection(3.5,5)).start()
    print ("processing")

    while True:
        mirai.engagementZone.processFirstZone()
        mirai.engagementZone.procesSecondZone()
