import threading
import time

class EngagementZones(object):

    personInZone1=False
    personInZone2=False

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALEngagementZones')
        self._proxy.subscribe("EngagementZoneSubscriber")
        self._pproxy = mirai.getProxy('ALPeoplePerception')
        self._pproxy.subscribe("PeoplePerceptionSubscriber2")
        self._memProxy = mirai.getProxy('ALMemory')
        self._personEnteredZone1 = False
        self._personEnteredZone2 = False
        self.start()

    def setFirstLimit(self,firsLimit,limitAngle):
        self._proxy.setFirstLimitDistance(firsLimit)
        self._proxy.setLimitAngle(limitAngle)

    def setSecondLimit(self,secondLimit,limitAngle):
        self._proxy.setSecondLimitDistance(secondLimit)
        self._proxy.setLimitAngle(limitAngle)

    def getFirstLimit(self):
        return self._proxy.getFirstLimitDistance()

    def getSecondLimit(self):
        return self._proxy.getSecondLimitDistance()

    def getAngle(self):
        return self._proxy.getlimitAngle()


    def zone1Callback(self,*args):
        self._mirai.mqttPublish('EngagementZone/enteredZone1')

    def zone2Callback(self,*args):
        self._mirai.mqttPublish('EngagementZone/enteredZone2')

    def movedAwayCallback(self,*args):
        self._mirai.mqttPublish('EngagementZone/movedAway')


    def processZones(self):
        print "processing"

        self.subscriber = self._memProxy.subscriber("EngagementZones/PersonEnteredZone1")
        self.subscriber.signal.connect(self.zone1Callback)
        self.subscriber1 = self._memProxy.subscriber("EngagementZones/PersonEnteredZone2")
        self.subscriber1.signal.connect(self.zone2Callback)


        self.subscriber2 = self._memProxy.subscriber("EngagementZones/PersonMovedAway")
        self.subscriber2.signal.connect(self.movedAwayCallback)

    def start(self):
        print "engage gestart"
        thread = threading.Thread(target=self.processZones)
        thread.start()

