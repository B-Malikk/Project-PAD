import threading
import time


class PeoplePerception(object):

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALPeoplePerception')
        self._memProxy = mirai.getProxy('ALMemory')
        self._peopleList = []
        self.newPersonDetected = False
        self.newPersonID=None
        self.startPeopleDetection()

    def setRange(self, range):
        self._proxy.setMaximumDetectionRange(range)

    def setDisappearTime(self, time):
        self._proxy.setTimeBeforePersonDisappears(time)
        self._proxy.setTimeBeforeVisiblePersonDisappears(time)

    def reset(self):
        self._proxy.resetPopulation()

    def startPeopleDetection(self):
        self.reset()#reset people population and counter

        #give callback when event rises
        #self._memProxy.subscribeToEvent('PeoplePerception/JustArrived', 'this', 'arrivedCallback')
        self.subscriber=self._memProxy.subscriber('PeoplePerception/JustArrived')
        self.subscriber.signal.connect(self.arrivedCallback)

        # give callback when event rises
        #self._memProxy.subscribeToEvent('PeoplePerception/JustLeft', 'this', 'leftCallback')
        #self.subscriber1=self._memProxy.subscriber('PeoplePerception/JustLeft')
        #self.subscriber1.signal.connect(self.leftCallback)
        threading.Thread(target=self.procesPeople).start()

    def arrivedCallback(self,id):
        print "new person"
        self.newPersonDetected = True
        self.newPersonID= id
        time.sleep(5)
        self.newPersonDetected = False


    def getNewPersonDistance(self):
        try:
            return self._memProxy.getData("PeoplePerception/Person/" + str(self.newPersonID) + "/Distance")
        except:
            pass




    def procesPeople(self):
        #stay looping to check if second boolean is true or false
        print ("in procespeople")
        while True:
            # save al ID's from visible poeple in an list
            self._peopleList = self._memProxy.getData("PeoplePerception/VisiblePeopleList")
            #if there are more than 1 person visible run the code
            while (len(self._peopleList) >=2):
                #save al ID's from visible poeple in an list
                print "dit is people list"
                print self._peopleList
                distanceList=[]
                for person in self._peopleList:
                    # get the distance from al the visible poeple
                    try:
                        distance = self._memProxy.getData("PeoplePerception/Person/" + str(person) + "/Distance")
                        distanceList.append(distance)
                    except:
                        pass

                print "dit is distance list"
                print distanceList

                def tooClose(givenDistance, distanceList):
                    for distance in distanceList:
                        range = [distance - .75, distance + .75]
                        if givenDistance > range[0] and givenDistance < range[1]:
                            return True
                    return False

                for distance in distanceList:
                    if tooClose(distance, distanceList):
                        print(" je staat te dichtbij")
                        self._mirai.textToSpeech.say("Houden jullie rekening met de annderhalve meter")
                        break
