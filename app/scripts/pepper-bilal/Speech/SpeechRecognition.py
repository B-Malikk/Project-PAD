from datetime import time
from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "localhost", 3629)
tts.say("speech")

Memory = ALProxy("ALMemory", "localhost", 3629)
SpeechRecognition = ALProxy("ALSpeechRecognition", "localhost",3629)


SpeechRecognition.setLanguage("Dutch")
tts.say("speech")


vocabulary = ["goedenmorgen","doei"]
SpeechRecognition.pause(0)  # pause the ASR engine to be able to call `setVocabulary()`
SpeechRecognition.setVocabulary(vocabulary, False)
SpeechRecognition.pause(1)  # restart the ASR engine

print 'Speech recognition engine started'
SpeechRecognition.subscribe("Test")

while True:
        gehoord = Memory.getData("WordRecognized")
        tts.say("You said")
        tts.say(gehoord[0])

        # sorting responses
        vocabulary = ["goedenmorgen", "doei"]

        if gehoord[0] is vocabulary[0]:
            tts.say("goedemorgen bilal")
        if gehoord[0] is vocabulary[1]:
            tts.say("doei doei")
            SpeechRecognition.unsubscribe("Test_ASR")
            break
