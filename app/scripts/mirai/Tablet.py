class Tablet(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALTabletService')


    def openPage(self,url):
        self._proxy.showWebview(url)

    def closePage(self):
        self._proxy.hideWebview()

    def reload(self):
        self._proxy.resetTablet()