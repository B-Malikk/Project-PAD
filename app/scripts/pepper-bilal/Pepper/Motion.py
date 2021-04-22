


class Motion:
    session  = motion_services = None



    def __init__(self,session):
        self.session = session
        # Get the services
        self.motion_services = self.session.service("ALMotion")


    def wakeup(self):
        self.motion_services.wakeUp()
        print("wake up")

    def sleep(self):
        self.motion_services.rest()
        print("slaap")