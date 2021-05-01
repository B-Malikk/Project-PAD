

class EngagementZones (object):




    def __init__(self,mirai):
        self._proxy = mirai.getProxy('ALEngagementZones')
        self._memProxy = mirai.getProxy('ALMemory')

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
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone1',self.firstZoneCallback())

    def firstZoneCallback(self):
        print("person detected in zone 1")


    def procesSecondZone(self):
        self._memProxy.subscribeToEvent('EngagementZones/PersonEnteredZone2',self.secondZoneCallback())

    def secondZoneCallback(self):
        print("person detected in zone 2")

