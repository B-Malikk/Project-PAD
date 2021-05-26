class TextToSpeech(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALTextToSpeech")
        self._aniProxy = mirai.getProxy("ALAnimatedSpeech")
        self.setLanguage("Dutch")
        self._language = self.getLanguage()
        self._speed = 100
        self.setSpeed(self._speed)

    def setLanguage(self, language):
        supported = self._proxy.getAvailableLanguages()
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported))
        self._proxy.setLanguage(language)
        self._language = language

    def getLanguage(self):
        return self._proxy.getLanguage()

    def setSpeed(self, speed):
        self._proxy.setParameter('speed', speed)
    def setVolume(self,volume):
        self._proxy.setVolume(volume)

    def say(self, text, language=None):
            if not language:
                language = self._language

            try:
                self._proxy.say(text, language)
            except:
                raise Exception("{} language is not installed.".format(language))

    def sayAnimated(self, text, mode=None):
        # See http://doc.aldebaran.com/2-5/naoqi/audio/alanimatedspeech.html
        if not mode:
            self._aniProxy.say(text)
        else:
            # Mode can be one of: disabled, random, or contextual
            valid_modes = ['disabled', 'random', 'contextual']
            if mode not in valid_modes:
                raise Exception("Given mode was not valid. Mode can only be one of {}.".format(valid_modes))
            self._aniProxy.say(text, {"bodyLanguageMode": mode})