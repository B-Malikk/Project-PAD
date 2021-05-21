import threading
import time
import math
from datetime import datetime


class Person(object):
    id = None
    distance = None
    pitchAngle = None
    yawAngle = None
    lastSeen = None

    def __init__(self, data):
        self.id = data[0]
        self.distance = data[1]
        self.pitchAngle = data[2]
        self.yawAngle = data[3]
        self.seen()

    def seen(self):
        self.lastSeen = datetime.utcnow()

    def equals(self, person):
        return person.id == self.id

    def __str__(self):
        return "ID: {}, distance: {}".format(self.id, int(self.distance*10)/10)

class PeoplePerception(object):

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALPeoplePerception')
        self._proxy.subscribe("PeoplePerceptionSubscriber") # This is needed for it to work!

        self._memProxy = mirai.getProxy('ALMemory')
        self._peopleList = []

        self.startPeopleDetection()

    def setRange(self, range):
        self._proxy.setMaximumDetectionRange(range)

    def setDisappearTime(self, time):
        self._proxy.setTimeBeforePersonDisappears(time)
        self._proxy.setTimeBeforeVisiblePersonDisappears(time)

    def reset(self):
        self._proxy.resetPopulation()

    def startPeopleDetection(self):
        self.reset()
        threading.Thread(target=self.processPeople).start()

    def arrivedCallback(self, person):
        print("arrivedCallback")
        self._mirai.textToSpeech.say("welkom")


    def leftCallback(self, person):
        print("leftCallback")
        self._mirai.textToSpeech.say("doei")

    def processPeople(self):
        while True:
            # add visible people to self._peopleList
            visiblePeople = self._memProxy.getData("PeoplePerception/VisiblePeopleList")
            peopleDetected = self._memProxy.getData("PeoplePerception/PeopleDetected")
            if peopleDetected:
                peopleDetected = peopleDetected[1]
                for data in peopleDetected:
                    person = Person(data)
                    if person.id in visiblePeople:
                        self.addPerson(person) # calls arrivedCallback()

            # update last seen timestamp for visible people
            for personId in visiblePeople:
                person = self.findPerson(personId)
                person.seen()

            # remove people who aren't visible for a while
            for person in self._peopleList:
                diff = datetime.utcnow() - person.lastSeen
                if person.id not in visiblePeople and diff.seconds > 0.5:
                    self._peopleList.remove(person)
                    self.leftCallback(person) # calls leftCallback()

    def findPerson(self, id):
        for person in self._peopleList:
            if person.id == id:
                return person
        return False

    def addPerson(self, personToAdd):
        for person in self._peopleList:
            if person.id == personToAdd.id:
                return
        self._peopleList.append(personToAdd)
        self.arrivedCallback(personToAdd)
