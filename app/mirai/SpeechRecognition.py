import time
import threading
class SpeechRecognition(object):
    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALSpeechRecognition')
        self._memProxy = mirai.getProxy('ALMemory')
        self._vocabulary = None
        #self._audioExpression = self.getAudioExpression()
        self._visualExpression = True
        #self.setVisualExpression(True)
        self._language = self.getLanguage()
        self._subscriptionName = 'MiraiSpeechRecognition'
        self._speechRecognitionstarted=False
        self._word=None


    def cleareMemory(self):
        try:
            self._memProxy.removeData("WordRecognized")
        except:
            pass

    def setVocabulary(self, vocabulary, wordSpotting=False):
        self._proxy.pause(True)
        self._proxy.setVocabulary(vocabulary, wordSpotting)
        self._proxy.pause(False)

    def getLanguage(self):
        return self._proxy.getLanguage()

    def setLanguage(self, language):
        self._proxy.pause(True)
        supported = self._proxy.getAvailableLanguages()
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported))
        self._proxy.setLanguage(language)
        self._language = language
        self._proxy.pause(False)

    def startSpeecheRecognition(self):
        print "speech started"
        try:
            self._proxy.unsubscribe("Test")
        except:
            pass
        self._proxy.subscribe("Test")
        self._speechRecognitionstarted = True
        threading.Thread(target=self.recognizeWord).start()


    def recognizeWord(self):
        while self._speechRecognitionstarted:
            try:
                self._memProxy.removeData("WordRecognized")
            except:
                pass

            try:
                recognize = self._memProxy.getData("WordRecognized")

                self._word = recognize[0]
                print self._word
                return self._word
            except:
                pass

    def stop(self):
        self._speechRecognitionstarted = False
        try:
            self._proxy.unsubscribe(self._subscriptionName)
        except:
            pass