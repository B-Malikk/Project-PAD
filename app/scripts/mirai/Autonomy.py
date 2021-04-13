#ALAutonomousBlinking
#   Enables the robot to make its eye LEDs blink when it sees someone and when it is interacting.
#ALBackgroundMovement
#   Defines which slight movements the robot does autonomously when its limbs are not moving.
#ALListeningMovement
#   Enables some slight movements showing that the robot is listening.
#ALSpeakingMovement
#   Enables to start autonomously movements during the speech of the robot.

class Ability(object):
    service = 'ALService'

    def __init__(self, session):
        self.session = session
        self.proxy = session.service(self.service)

    def enable(self):
        self.proxy.setEnabled(True)

    def disable(self):
        self.proxy.setEnabled(False)

    def isEnabled(self):
        return self.proxy.isEnabled()

    def isRunning(self):
        return self.proxy.isRunning()

    def __str__(self):
        return "(Ability: {}, isEnabled: {}, isRunning: {})".format(self.__class__.__name__, self.isEnabled(), self.isRunning())

class Blinking(Ability):
    service = 'ALAutonomousBlinking'

class Background(Ability):
    service = 'ALBackgroundMovement'

class Listening(Ability):
    service = 'ALListeningMovement'

class Speaking(Ability):
    service = 'ALSpeakingMovement'

class AutonomousMovement(object):
    def __init__(self, session):
        self.movements = {
            'blink': Blinking(session),
            'background': Background(session),
            'listen': Listening(session),
            'speak': Speaking(session),
        }
    def list(self):
        return self.movements

    def get(self, name):
        item = self.movements.get(name, None)
        if not item:
            raise Exception("{} was not found. Did you mean any of the following?\n".format(name) +
                str(self.movements.keys())
            )
        return item