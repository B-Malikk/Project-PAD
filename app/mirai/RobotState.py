"""  The class  allows you to get and set the robot state. """

class RobotState(object):


    def __init__(self,mirai):
        self.currentPosture = 'open' #Default state

    def getPosture(self):
        return self.currentPosture  #Returs the current state

    def setPosture(self, postureName): #Setter for changing the state of the robot
        self.currentPosture = postureName