import threading
import time

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


    def setInfoZone1a(self,val):
        print("person entered zone 1")
        if val != []:  # als value niet leeg is dan is er iemand in zone 1
            self.personInZone1 = True
        elif val == []:
            self.personInZone1 = False

    def setInfoZone1b(self,val):
        if val != []:  # als value niet leeg is dan heeft iemand zone 1 verlaten
            self.personInZone1 = False

    def processZones(self):
        print "processing"
        while True:
            self.subscriber = self._memProxy.subscriber("EngagementZones/PersonEnteredZone1")
            self.subscriber.signal.connect(self.setInfoZone1a)
            print (" in while")

            self.subscriber1 = self._memProxy.subscriber("EngagementZones/PersonMovedAway")
            self.subscriber1.signal.connect(self.setInfoZone1b)

    def start(self):
        print "engage gestart"
        thread = threading.Thread(target=self.processZones)
        thread.start()

