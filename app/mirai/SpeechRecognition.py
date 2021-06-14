import time
import threading



""""The class allows you set a vocubalry and recognise if something is heard"""

class SpeechRecognition(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALSpeechRecognition')
        self._memProxy = mirai.getProxy('ALMemory')
        self._vocabulary = None
        self._language = self.getLanguage()
        self._subscriptionName = 'MiraiSpeechRecognition'
        self._speechRecognitionstarted=False
        self._word=None


    def cleareMemory(self):
        self._memProxy.removeData("WordRecognized")

    def setVocabulary(self, vocabulary, wordSpotting=False):
        self._proxy.pause(True)#First pause the ASR when changing something
        self._proxy.setVocabulary(vocabulary, wordSpotting) # set an list of vocubalary and by default set wordspotting false
        self._proxy.pause(False)#Restart the ASR engine after an chaning

    def getLanguage(self):
        return self._proxy.getLanguage()

    def setLanguage(self, language):
        self._proxy.pause(True)# first pause the ASR when changing something
        supported = self._proxy.getAvailableLanguages()# get al available languages from the robot
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported)) # raise exception when language is not suported
        self._proxy.setLanguage(language)
        self._language = language
        self._proxy.pause(False)# Restart the ASR engine after any changing

    #starts the process speechrecognised
    def startSpeecheRecognition(self):
        try:
            self._proxy.unsubscribe("Test") # unsubscribe if already is subscribed else pass
        except:
            pass
        self._proxy.subscribe("Test")
        self._speechRecognitionstarted = True
        threading.Thread(target=self.recognizeWord).start()


    #Returns the recognised word
    def recognizeWord(self):
        while self._speechRecognitionstarted:
            try: #try if nothing is recognised than pass
                recognize = self._memProxy.getData("WordRecognized")

                self._word = recognize[0]
                print self._word
                return self._word
            except:
                pass

    #Stop the speechrecognition and unsubsubcribe the topic
    def stop(self):
        self._speechRecognitionstarted = False
        self._proxy.unsubscribe(self._subscriptionName)
