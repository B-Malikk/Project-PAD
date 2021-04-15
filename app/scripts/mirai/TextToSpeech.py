class TextToSpeech(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALTextToSpeech")
        self.getLanguage() # sets self._language
        self._speed = 100
        self.setSpeed(self._speed)

    def setLanguage(self, language):
        supported = self._proxy.getSupportedLanguages()
        if language not in supported:
            raise Exception("Language is not supported! Only the following languages can be used: {}".format(supported))
        self._proxy.setLanguage(language)
        self._language = language

    def getLanguage(self):
        lang = self._proxy.getLanguage()
        self._language = lang
        return lang

    def setSpeed(self, speed):
        self._proxy.setParameter('speed', speed)

    def say(self, text, language=None):
            if not language:
                language = self._language

            try:
                self._proxy.say(text, language)
            except:
                raise Exception("{} language is not installed.".format(language))

