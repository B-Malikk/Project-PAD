import threading


class EngagementZones(object):
    personInZone1=False
    personInZone2=False

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALEngagementZones')
        self._memProxy = mirai.getProxy('ALMemory')
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

    def processFirstZone(self):
        # give callback when event rises(person in zone 1)
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone1','EngagementZones','setInfoZone1a')

        #subscriber1 = self._memProxy.subscriber('EngagementZones/PersonEnteredZone1')
        #subscriber1.signal.connect(self.setInfoZone1a())
        # give callback when event rises(person left zone 1)
        self._memProxy.subscribeToEvent('EngagementZones/PersonMovedAway', 'EngagementZones', 'setInfoZone1b')
        #subscriber2=self._memProxy.subscriber('EngagementZones/PersonMovedAway')
        #subscriber2.signal.connect(self.setInfoZone1b())

    def getInfoZone1(self):
        return self.personInZone1

    def setInfoZone1a(self):
        self.personInZone1=True
    def setInfoZone1b(self):
        self.personInZone1=False

    def procesSecondZone(self):
        # give callback when event rises(person in zone 2)
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone2', 'EngagementZones', 'setInfoZone2a')
        #subscriber1=self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone2')
        #subscriber1.signal.connect(self.setInfoZone2a())
        # give callback when event rises(person left zone 2)
        self._memProxy.subscribeToEvent('EngagementZones/PersonMovedAway', 'EngagementZones', 'setInfoZone2b')
        #subscriber2=self._memProxy.subscribeToEvent('EngagementZones/PersonMovedAway')
        #subscriber2.signal.connect(self.setInfoZone2b())

    def getInfoZone2(self):
        return self.personInZone2

    def setInfoZone2a(self):
        self.personInZone2=True
    def setInfoZone2b(self):
        self.personInZone2=False

    def processZones(self):
        while True:
            self._mirai.engagementZone.processFirstZone()
            self._mirai.engagementZone.procesSecondZone()

    def start(self):
        threading.Thread(target=self.processZones()).start()

