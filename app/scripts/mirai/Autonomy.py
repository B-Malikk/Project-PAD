#ALAutonomousBlinking
#   Enables the robot to make its eye LEDs blink when it sees someone and when it is interacting.
#ALBackgroundMovement
#   Defines which slight movements the robot does autonomously when its limbs are not moving.
#ALListeningMovement
#   Enables some slight movements showing that the robot is listening.
#ALSpeakingMovement
#   Enables to start autonomously movements during the speech of the robot.

class Ability(object):
    _service = 'AL_Service'

    def __init__(self, mirai):
        self._proxy = mirai.getProxy(self._service)

    def enable(self):
        self._proxy.setEnabled(True)

    def disable(self):
        self._proxy.setEnabled(False)

    def isEnabled(self):
        return self._proxy.isEnabled()


    def __str__(self):
        return "(Ability: {}, isEnabled: {})".format(self.__class__.__name__, self.isEnabled())

class Blinking(Ability):
    _service = 'ALAutonomousBlinking'

class Background(Ability):
    _service = 'ALBackgroundMovement'

class Listening(Ability):
    _service = 'ALListeningMovement'

class Speaking(Ability):
    _service = 'ALSpeakingMovement'

    MODE_RANDOM = 'random'
    MODE_CONTEXTUAL = 'contextual'

    def setMode(self, mode):
        self._proxy.setMode(mode)

    def getMode(self):
        self._proxy.getMode()

class AutonomousMovement(object):
    def __init__(self, session):
        self.blink =  Blinking(session)
        self.background = Background(session)
        self.listen =  Listening(session)
        self.speak = Speaking(session)
