import threading
import time

class EngagementZones(object):
    personInZone1=False
    personInZone2=False

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALEngagementZones')
        self._memProxy = mirai.getProxy('ALMemory')
        #self._memProxy.subscriber('ALPeoplePerception')
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone1','self','setInfoZone1a')
        self._memProxy.subscribeToEvent('EngagementZones/PersonMovedAway', 'self', 'setInfoZone1b')
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone2', 'self', 'setInfoZone2a')
        self._memProxy.subscribeToEvent('EngagementZones/PersonMovedAway', 'self', 'setInfoZone2b')
        self.start()

    def setFirstLimit(self,firsLimit,limitAngle):
        self._proxy.setFirstLimitDistance(firsLimit)
        self._proxy.setLimitAngle(limitAngle)

    def setSecondLimit(self, secondLimit,limitAngle):
        self._proxy.setSecondLimitDistance(secondLimit)
        self._proxy.setLimitAngle(limitAngle)

    def getFirstLimit(self):
        return self._proxy.getFirstLimitDistance()

    def getSecondLimit(self):
        return self._proxy.getSecondLimitDistance()

    def getAngle(self):
        return self._proxy.getlimitAngle()


    def getInfoZone1(self):
        return self.personInZone1

    def setInfoZone1a(self, id, val, msg):
        print("person entered zone 1")
        self.personInZone1 = True

    def setInfoZone1b(self,value):
        print("person left zone 1")
        self.personInZone1 = False

    def getInfoZone2(self):
        return self.personInZone2

    def setInfoZone2a(self):
        print("person entered zone 2")
        self.personInZone2=True
    def setInfoZone2b(self):
        print("person left zone 2")
        self.personInZone2=False

    def processZones(self):
        while True:
            time.sleep(.1)

    def start(self):
        thread = threading.Thread(target=self.processZones)
        thread.start()

