import time
import threading

class SpeechRecognition(object):
    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALSpeechRecognition')
        self._memProxy = mirai.getProxy('ALMemory')
        self._vocabulary = None
        self._audioExpression = self.getAudioExpression()
        self._visualExpression = True
        self.setVisualExpression(True)
        self._language = self.getLanguage()
        self._subscriptionName = 'MiraiSpeechRecognition'
        self._speechRecognitionstarted=False

    def setVocabulary(self, vocabulary, wordSpotting=False):
        self._proxy.setVocabulary(vocabulary, wordSpotting)

    def getAudioExpression(self):
        self._audioExpression = self._proxy.getAudioExpression()
        return self._audioExpression

    def getVisualExpression(self):
        return self._visualExpression

    def setAudioExpression(self, bool):
        self._proxy.setAudioExpression(bool)

    def setVisualExpression(self, bool):
        self._proxy.setVisualExpression(bool)

    def getLanguage(self):
        return self._proxy.getLanguage()

    def setLanguage(self, language):
        supported = self._proxy.getAvailableLanguages()
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported))
        self._proxy.setLanguage(language)
        self._language = language

    def startSpeecheRecognition(self):
        try:
            self._proxy.unsubscribe("Test")
        except:
            pass
        self._proxy.setVocabulary(self._vocabulary, False)
        self._proxy.subscribe("Test")
        self.speech_recognition_started = True
        threading.Thread(target=self.recognizeWord).start()

    def recognizeWord(self):
        while self._speechRecognitionstarted:
            recognize = self._memProxy.getData("WordRecognized")

            word = recognize[0]
            print word
            return word

    #def recognizeWord(self, debug=False):
        #if not self._vocabulary:
            #raise Exception("No vocabulary has been set yet.")
        #if debug:
            #print("vocab: {}\nexpression: {}\nlanguage: {}".format(self._vocabulary, self._expression, self._language))

        #self._proxy.subscribe(self._subscriptionName)

        #recognized = None
        #while not recognized:
            #try:
                #words = self._memProxy.getData("WordRecognized")
                #if debug:
                    #prnt(words)

                #recognized = words[0]
        #except:
                #time.sleep(.1)
                #continue

        #self._proxy.unsubscribe(self._subscriptionName)
        #return recognized

    def stop(self):
        self._speechRecognitionstarted = False
        try:
            self._proxy.unsubscribe(self._subscriptionName)
        except:
            pass