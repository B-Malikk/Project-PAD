#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to get & read FaceDetected Events"""

import qi
import time
import sys
import argparse

from naoqi import ALProxy

global x
x = True

joint = ALProxy("ALMotion", "mirai.robot.hva-robots.nl",9559 )
tts = ALProxy("ALTextToSpeech", "mirai.robot.hva-robots.nl",9559)
posture_service = ALProxy("ALRobotPosture", "mirai.robot.hva-robots.nl",9559)
tts.setLanguage("Dutch")

tts.say("kaas")

def wave():
    # Wave met linker arm
    tts.say("Hallo!")
    names = ["LShoulderRoll", "LShoulderPitch", "LWristYaw"]
    elbow = ["LElbowRoll"]
    angleLists = [1.6, -0.5, -0.5]
    angleElbow = [-2.0, -0.5, -2, 0]
    times = [0.4, 0.6, 0.8, 1.0]
    elbowtimes = [0.2, 0.6, 1.0, 1.4]
    isAbsolute = True
    joint.angleInterpolation(names, angleLists, times, isAbsolute)
    joint.angleInterpolation(elbow, angleElbow, elbowtimes, isAbsolute)
    posture_service.goToPosture("StandInit", 0.7)
    tts.say("Welcom in het Wibauthuis")
    global x
    x = False



class HumanGreeter(object):
    """
    A simple class to react to face detection events.
    """
    is_greeting = False
    got_face = False


    def __init__(self, app):
        """
        Initialisation of qi framework and event detection.
        """
        super(HumanGreeter, self).__init__()
        app.start()
        session = app.session
        # Get the service ALMemory.
        self.memory = session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("FaceDetected")
        self.subscriber.signal.connect(self.on_human_tracked)
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = session.service("ALTextToSpeech")
        self.face_detection = session.service("ALFaceDetection")
        self.face_detection.subscribe("HumanGreeter")
        self.got_face = False

    def on_human_tracked(self, value):
        """
        Callback for event FaceDetected.
        """
        if not self.got_face and value != []:  # only speak the first time a face appears
            if not self.is_greeting:
                self.is_greeting = True
                self.got_face = True
                print "I saw a face!"
                wave()  #wave if a face is seen



                # First Field = TimeStamp.
                timeStamp = value[0]
                print "TimeStamp is: " + str(timeStamp)

                # Second Field = array of face_Info's.
                faceInfoArray = value[1]
                for j in range(len(faceInfoArray) - 1):
                    faceInfo = faceInfoArray[j]

                    # First Field = Shape info.
                    faceShapeInfo = faceInfo[0]

                    # Second Field = Extra info (empty for now).
                    faceExtraInfo = faceInfo[1]

                    print "Face Infos :  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
                    print "Face Infos :  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])
                    print "Face Extra Infos :" + str(faceExtraInfo)
                self.is_greeting = False

        self.got_face = (value)

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """

        print "Starting HumanGreeter"
        try:
            while True:
                time.sleep(.01)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping HumanGreeter"
            self.face_detection.unsubscribe("HumanGreeter")
            # stop
            sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="mirai.robot.hva-robots.nl",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    try:
        # Initialize qi framework.
        from naoqi import ALProxy

        motion = ALProxy("ALMotion", args.ip, args.port)
        motion.moveInit()
        motion.wakeUp()
        connection_url = "tcp://" + args.ip + ":" + str(args.port)
        app = qi.Application(["HumanGreeter", "--qi-url=" + connection_url])
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                              "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    human_greeter = HumanGreeter(app)
    human_greeter.run()
