import time
import argparse
import qi
from naoqi import ALProxy
from Pepper import speechRecognition
from Pepper import TxtToSpeech
from Pepper import faceDetection
from Pepper import Tablet


def q0(session):
    fd = faceDetection.FaceDetection(session)
    sr = speechRecognition.SpeechRecognition(session)
    sr.setTaal("Dutch")
    print ("ben bij vraag 4")
    tts.say("heb je nog meer vragen ")

    sr.startSpeecheRecognition()
    while not (sr.processSpeechRecognition() == 'ja' or sr.processSpeechRecognition() == 'nee'):
        time.sleep(1)

    if sr.processSpeechRecognition() == 'ja':
        sr.stop()
        q1(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        tts.say("okey fijne dag nog")

def q3(session):
    fd = faceDetection.FaceDetection(session)
    sr = speechRecognition.SpeechRecognition(session)
    print ("ben bij vraag 3")
    sr.setTaal("Dutch")
    time.sleep(1)
    tts.say("heb je vragen over je hva pas? ")

    sr.startSpeecheRecognition()
    while not (sr.processSpeechRecognition() == 'ja' or sr.processSpeechRecognition() == 'nee'):
        time.sleep(1)

    if sr.processSpeechRecognition() == 'ja':
        sr.stop()
        tts.say("hiervoor verwijz ik je door naar de balie ")
        time.sleep(3)
        q0(session)

    if sr.processSpeechRecognition() == 'nee':
        tts.say("dan weet ik het ook niet succes ")
        sr.stop()


def q2(session):
    fd = faceDetection.FaceDetection(session)
    sr = speechRecognition.SpeechRecognition(session)
    print ("ben bij vraag 2")
    sr.setTaal("Dutch")
    time.sleep(1)
    tts.say("wil je weten waar je lokaal is? ")

    sr.startSpeecheRecognition()
    while not (sr.processSpeechRecognition() == 'ja' or sr.processSpeechRecognition() == 'nee'):
        time.sleep(1)

    if sr.processSpeechRecognition() == 'ja':
        sr.stop()
        tts.say("typ op het tablet je lokaal nummer ")
        time.sleep(3)
        q0(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        q3(session)

def q1(session):
    fd = faceDetection.FaceDetection(session)
    sr = speechRecognition.SpeechRecognition(session)
    print ("ben bij vraag 1")
    sr.setTaal("Dutch")
    time.sleep(1)
    tts.say("wil je weten waar je bent ")

    sr.startSpeecheRecognition()
    while not (sr.processSpeechRecognition() == 'ja' or sr.processSpeechRecognition() == 'nee'):
        time.sleep(1)

    if sr.processSpeechRecognition() == 'ja':
        sr.stop()
        tts.say("je bent nu in het HVA Wibauthuis aan de wibautstraat")
        q1(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        q2(session)

def askForHelp (session):
    fd = faceDetection.FaceDetection(session)
    sr= speechRecognition.SpeechRecognition(session)
    tijdLimiet = 10
    startTijd = time.time()

    sr.setTaal("Dutch")
    print ("ben bij vraag 0")
    tts.say("kan ik je ergens me helpen")
    sr.startSpeecheRecognition()


    while not (sr.processSpeechRecognition() == 'ja' or sr.processSpeechRecognition() == 'nee'):
        time.sleep(1)

    if sr.processSpeechRecognition() == 'ja':
        sr.stop()
        q1(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        tts.say("okey fijne dag nog")

    gespeeldTijd = time.time() - startTijd

    if gespeeldTijd >= tijdLimiet:
        sr.stop()







if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="mirai.robot.hva-robots.nl",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    mirai="mirai.robot.hva-robots.nl"
    poort=9559

    session = qi.Session()
    session.connect("tcp://" + args.ip + ":" + str(args.port))
    tts=TxtToSpeech.txtToSpeech(session)
    tts.say("sii")
    tablet=Tablet.Tablet(session)
    tablet.openPage("https://oege.ie.hva.nl/~polmpm/hoofdpagina.html")
    askForHelp(session)





