import time

class Tablet:
    session = tablet_service = None

    def __init__(self, session):
        self.session = session
        self.tablet_service = self.session.service("ALTabletService")


    def open_page(self,url):
        self.tablet_service.showWebview(url)

    def close_page(self):
        self.tablet_service.hideWebview()

    def reload(self):
        self.tablet_service.resetTablet()


