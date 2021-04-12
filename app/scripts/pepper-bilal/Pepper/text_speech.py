

class TextToSpeech:
    session = tts_service = None

    def __init__(self, session):
        self.session = session
        self.tts_service = self.session.service("ALTextToSpeech")

    def say(self, txt):
        self.tts_service.say(txt)
        return self
