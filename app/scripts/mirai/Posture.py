class Posture(object):
    """Base class for a posture"""
    def __init__(self, mirai):
        self.name = self.__class__.__name__
        self.proxy = mirai.getProxy("ALRobotPosture")

    def apply(self, blocking=True):
        if not blocking:
            self.proxy.post.goToPosture(self.name, 1.0)
        else:
            self.proxy.goToPosture(self.name, 1.0)

class StandInit(Posture):
    pass

class StandZero(Posture):
    pass

class Crouch(Posture):
    pass

class Postures(object):
    def __init__(self, mirai):
        self.StandInit = StandInit(mirai)
        self.StandZero = StandZero(mirai)
        self.Crouch = Crouch(mirai)