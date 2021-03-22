import time

class Tablet:
    session = tabletService = None

    def __init__(self, session):
        self.session = session
        self.tabletService = self.session.service("ALTabletService")

        self.tabletService.enableWifi()
        self.tabletService.showWebview("http://198.18.0.1/apps/mirai/video_idle.html")

    def openPage(self,url):
        self.tabletService.showWebview(url)

    def closePage(self):
        self.tabletService.hideWebview()


