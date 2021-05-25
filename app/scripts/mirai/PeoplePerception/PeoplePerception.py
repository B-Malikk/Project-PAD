import threading
import time
import math
from datetime import datetime

class Position(object):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(x: {:.2f}, y: {:.2f})".format(self.x, self.y)

class Person(object):
    id = None
    distance = None
    pitchAngle = None
    yawAngle = None
    lastSeen = None

    rawData = None
    position = None

    def __init__(self, data):
        self.id = data[0]
        self.update(data)
        self.rawData = data

    def seen(self):
        self.lastSeen = datetime.utcnow()

    def update(self, data):
        self.distance = data[1]
        self.pitchAngle = math.degrees(data[2])
        self.yawAngle = math.degrees(data[3])
        self.seen()
        self.updatePosition()

    def equals(self, person):
        return person.id == self.id

    def updatePosition(self):
        angleA = math.radians(90)
        angleB = math.radians(self.yawAngle if self.yawAngle > 0 else -1*self.yawAngle)

        distanceA = self.distance
        distanceB = (distanceA / math.sin(angleA)) * math.sin(angleB)
        angleC = math.radians(180 - math.degrees(angleA) - math.degrees(angleB))
        distanceC = (distanceA / math.sin(angleA)) * math.sin(angleC)

        x = distanceB if self.yawAngle > 0 else -1*distanceB
        y = distanceC
        self.position = Position(x, y)

    def distanceTo(self, person):
        x1 = self.position.x
        x2 = person.position.x

        y1 = self.position.y
        y2 = person.position.y
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    def __str__(self):
        return "Person (ID: {}, distance: {:.2f}m, pitch: {}, angle: {}, pos: {})".format(self.id, self.distance, self.pitchAngle, self.yawAngle, self.position)


class PeoplePerception(object):

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALPeoplePerception')

        self._memProxy = mirai.getProxy('ALMemory')
        self._peopleList = []

        threading.Thread(target=self.processPeople).start()

    def arrivedCallback(self, person):
        self._mirai.mqttPublish('PeoplePerception/personArrived', '')

    def leftCallback(self, person):
        self._mirai.mqttPublish('PeoplePerception/personLeft', '')

    def processPeople(self):
        while True:

            self._proxy.subscribe("PeoplePerceptionSubscriber")  # This is needed for it to work!
            # add visible people to self._peopleList
            visiblePeople = self._memProxy.getData("PeoplePerception/VisiblePeopleList")
            peopleDetected = self._memProxy.getData("PeoplePerception/PeopleDetected")
            if peopleDetected:
                peopleDetected = peopleDetected[1]
                for data in peopleDetected:
                    person = Person(data)
                    if person.id in visiblePeople:
                        self.addPerson(person) # calls arrivedCallback()
                        # updates last seen timestamp for visible people as well

            # remove people who aren't visible for a while
            for person in self._peopleList:
                diff = datetime.utcnow() - person.lastSeen
                if person.id not in visiblePeople and diff.seconds > 0.5:
                    self._peopleList.remove(person)
                    self.leftCallback(person) # calls leftCallback()

            #for person in self._peopleList:
            #    print(person)

            self.coronaProofing()

    def findPerson(self, id):
        for person in self._peopleList:
            if person.id == id:
                return person
        return False

    def addPerson(self, personToAdd):
        for person in self._peopleList:
            if person.id == personToAdd.id:
                person.update(personToAdd.rawData)
                return
        self._peopleList.append(personToAdd)
        self.arrivedCallback(personToAdd)
        return personToAdd

    def coronaProofing(self):
        def peopleAreTooClose():
            for person in self._peopleList:
                for otherPerson in self._peopleList:
                    if person.distanceTo(otherPerson) < 1.5:
                        return True
            return False

        if len(self._peopleList) >= 2:
            if peopleAreTooClose():
                self._mirai.mqttPublish('PeoplePerception/tooClose', '')
