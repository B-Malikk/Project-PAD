import threading
import time


""" The class  allows you to classify zones to detect people and/or movements using their position in space 
of the Mirai <pepper>"""



class EngagementZones(object):


    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALEngagementZones')
        self._proxy.subscribe("EngagementZoneSubscriber")
        self._pproxy = mirai.getProxy('ALPeoplePerception')
        self._pproxy.subscribe("PeoplePerceptionSubscriber2")
        self._memProxy = mirai.getProxy('ALMemory')
        self.start() # when the object is made start processing the zones

    def setFirstLimit(self,firsLimit,limitAngle): #sets the first limit and the angle for zone 1
        self._proxy.setFirstLimitDistance(firsLimit)
        self._proxy.setLimitAngle(limitAngle)

    def setSecondLimit(self,secondLimit,limitAngle): #sets the first limit and the angle for zone 2
        self._proxy.setSecondLimitDistance(secondLimit)
        self._proxy.setLimitAngle(limitAngle)

    def getFirstLimit(self):
        return self._proxy.getFirstLimitDistance() #returns the limit from zone 1

    def getSecondLimit(self):
        return self._proxy.getSecondLimitDistance() #returns the limit from zone 2

    def getAngle(self):
        return self._proxy.getlimitAngle() #returns the angle


    #Calbacks
    def zone1Callback(self,*args): #*args is used to pass a variable number of arguments to a function.
        self._mirai.mqttPublish('EngagementZone/enteredZone1', '') #publish an message on the MQTT

    def zone2Callback(self,*args):
        self._mirai.mqttPublish('EngagementZone/enteredZone2', '')

    def movedAwayCallback(self,*args):
        self._mirai.mqttPublish('EngagementZone/movedAway', '')


    def processZones(self):
        print "processing"

        self.subscriber = self._memProxy.subscriber("EngagementZones/PersonEnteredZone1") #Subscribe to an event
        self.subscriber.signal.connect(self.zone1Callback) #connect the subscribed event to the calback function

        self.subscriber1 = self._memProxy.subscriber("EngagementZones/PersonEnteredZone2")
        self.subscriber1.signal.connect(self.zone2Callback)


        self.subscriber2 = self._memProxy.subscriber("EngagementZones/PersonMovedAway")
        self.subscriber2.signal.connect(self.movedAwayCallback)

    def start(self):
        print "engage gestart"
        thread = threading.Thread(target=self.processZones)
        thread.start()

