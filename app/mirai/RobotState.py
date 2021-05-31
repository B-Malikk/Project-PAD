class RobotState(object):


    def __init__(self,mirai):
        self.currentPosture = 'open'

    def getPosture(self):
        return self.currentPosture

    def setPosture(self, postureName):
        self.currentPosture = postureName