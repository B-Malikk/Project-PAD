import argparse
import qi
from naoqi import ALProxy
from Pepper import speechRecognition
from Pepper import TxtToSpeech

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=1844,
                        help="Naoqi port number")

    args = parser.parse_args()
    mirai="mirai.robot.hva-robots.nl"
    poort=9559

    session = qi.Session()
    session.connect("tcp://" + args.ip + ":" + str(args.port))

    txtToSpeechh=TxtToSpeech.txtToSpeech
    txtToSpeechh.say()



