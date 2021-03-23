import time


class SpeechRecognition:
    session = speechRecognitionService = memoryService = tts = None
    speechRecognitionGestart = False
    woordenlijst = ["ja","nee"]
    laatsteRecognize = 0

    def __init__(self, session):
        self.session = session
        self.speechRecognitionService = self.session.service("ALSpeechRecognition")
        self.tts = self.session.service("ALTextToSpeech")
        self.memoryService = self.session.service("ALMemory")

    def setTaal(self,taal):
        self.speechRecognitionService.setLanguage(taal)
        return self

    def processSpeechRecognition(self):
        while self.speechRecognitionGestart:
            recognize = self.memoryService.getData("WordRecognized")
            word = recognize[0]
            print word
            return word


    def startSpeecheRecognition(self):
        try:
            self.speechRecognitionService.unsubscribe("Test")
        except:
            pass
        self.speechRecognitionService.setVocabulary(self.woordenlijst, False)
        self.speechRecognitionService.subscribe("Test")
        self.speechRecognitionGestart = True
        self.processSpeechRecognition()
        return self

    def stop(self):
        self.speechRecognitionGestart = False
        self.speechRecognitionService.unsubscribe("Test")

    def setWoordenLijst(self,woordenlijst):
        self.woordenlijst=woordenlijst
        return self

