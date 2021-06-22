class TextToSpeech(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALTextToSpeech")
        self._aniProxy = mirai.getProxy("ALAnimatedSpeech")
        self.setLanguage("Dutch")
        self._language = self.getLanguage()
        self._speed = 100
        self.setSpeed(self._speed)

    def setLanguage(self, language):
        # All available languages are collected and put in supported
        supported = self._proxy.getAvailableLanguages()
        # If language isn't available an exception is raised
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported))
        # Language is set to chosen language
        self._proxy.setLanguage(language)
        self._language = language

    def getLanguage(self):
        # The used language at that time will be returned
        return self._proxy.getLanguage()

    def setSpeed(self, speed):
        # speed is set to wanted speed
        self._proxy.setParameter('speed', speed)
    def setVolume(self,volume):
        # volume is set to wanted volume
        self._proxy.setVolume(volume)

    def say(self, text, language=None):
        # Text is said in selected language, if no language is chosen the last chosen language will be used
            if not language:
                language = self._language

            try:
                self._proxy.say(text, language)
            except:
                raise Exception("{} language is not installed.".format(language))

    def sayAnimated(self, text, mode=None):
        # See http://doc.aldebaran.com/2-5/naoqi/audio/alanimatedspeech.html
        # Text is said in chosen mode, if no mode is chosen the last chosed mode will be used. If chosen mode doesn't
        # exist an exception will be raised
        if not mode:
            self._aniProxy.say(text)
        else:
            # Mode can be one of: disabled, random, or contextual
            valid_modes = ['disabled', 'random', 'contextual']
            if mode not in valid_modes:
                raise Exception("Given mode was not valid. Mode can only be one of {}.".format(valid_modes))
            self._aniProxy.say(text, {"bodyLanguageMode": mode})