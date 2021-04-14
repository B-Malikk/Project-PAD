class TextToSpeech(object):

    def __init__(self, mirai):
        self.proxy = mirai.getProxy("ALTextToSpeech")
        #WIP