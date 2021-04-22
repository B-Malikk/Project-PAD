import time
from Pepper import speech_recognition
from Pepper import text_speech
from Pepper import face_detection
from Pepper import tablet
from Pepper import connect


def q0(session):
    sr = speech_recognition.SpeechRecognition(session)
    sr.setTaal("Dutch")
    print ("ben bij vraag 4")
    #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/hoofdpagina.html")
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
    sr = speech_recognition.SpeechRecognition(session)
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
        #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/pasje")
        time.sleep(3)
        q0(session)

    if sr.processSpeechRecognition() == 'nee':
        tts.say("dan weet ik het ook niet succes ")
        sr.stop()


def q2(session):
    sr = speech_recognition.SpeechRecognition(session)
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
        #tablet.openPage("https://oege.ie.hva.nl/~polmpm/robot/lokaal zoeken.html")
        time.sleep(3)
        q0(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        q3(session)

def q1(session):

    sr = speech_recognition.SpeechRecognition(session)
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
        #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/plattegrond.html")
        q1(session)

    if sr.processSpeechRecognition() == 'nee':
        sr.stop()
        q2(session)

def askForHelp (session):

    sr= speech_recognition.SpeechRecognition(session)
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

    ip = "mirai.robot.hva-robots.nl"
    port = 9559

    pepper = connect.Connect(ip,port)
    session = pepper.make_connection()

    #get services en geef de session mee
    tts=text_speech.TextToSpeech(session)
    #tts.say("ik meet nu de afstand")


    tts = text_speech.TextToSpeech(session)
    #tts.say("test")

    fd = face_detection.FaceDetection(session)
    fd.start_face_detection()
    print fd.process_face_detection()



    #tablet = tablet.Tablet(session)
    #tablet.reload()
    #tablet.open_page("https://oege.ie.hva.nl/~polmpm/robot/hoofdpagina.html")
    #tablet.close_page()
    #askForHelp(session)






