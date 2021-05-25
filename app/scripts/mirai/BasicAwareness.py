import time


class BasicAwareness(object):

    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALBasicAwareness')

    def setBA(self,bool):
        self._proxy.setEnabled(bool)

    def setEnagement(self,mode):# Unengaged ,FullyEngaged,SemiEngaged
        self._proxy.setEngagementMode(mode)

    def pausAwareness(self):
        self._proxy.pauseAwareness()

    def resumeAwareness(self):
        self._proxy.resumeAwareness()

