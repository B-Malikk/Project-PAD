import time


class SpeechRecognition:
    session = speech_recognition_service = memory_service = None
    speech_recognition_started = False
    vocubulary = ["ja","nee"]

    def __init__(self, session):
        self.session = session
        self.speech_recognition_service = self.session.service("ALSpeechRecognition")
        self.memoryService = self.session.service("ALMemory")

    def setTaal(self,language):
        self.speech_recognition_service.setLanguage(language)
        return self

    def processSpeechRecognition(self):
        while self.speechRecognitionGestart:
            recognize = self.memoryService.getData("WordRecognized")
            word = recognize[0]
            print word
            return word


    def startSpeecheRecognition(self):
        try:
            self.speech_recognition_service.unsubscribe("Test")
        except:
            pass
        self.speech_recognition_service.setVocabulary(self.vocubulary, False)
        self.speech_recognition_service.subscribe("Test")
        self.speech_recognition_started = True
        self.processSpeechRecognition()
        return self

    def stop(self):
        self.speechRecognitionGestart = False
        try:
            self.speech_recognition_service.unsubscribe("Test")
        except:
            pass

    def setWoordenLijst(self,vocubulary):
        self.vocubulary = vocubulary
        return self

