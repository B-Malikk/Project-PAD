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
        #threading.Thread(target=self.procesPeople).start()

    def arrivedCallback(self,id):
        print "new person"
        self.newPersonDetected = True
        self.newPersonID= id
        time.sleep(5)
        self.newPersonDetected = False


    def getNewPersonDistance(self):
        return self._memProxy.getData("PeoplePerception/Person/" + str(self.newPersonID) + "/Distance")




    def procesPeople(self):
        #stay looping to check if second boolean is true or false
        while True:
            # save al ID's from visible poeple in an list
            self._peopleList = self._memProxy.getData("PeoplePerception/VisiblePeopleList")
            #if there are more than 1 person visible run the code
            while (len(self._peopleList) >=2):
                #save al ID's from visible poeple in an list
                print "dit is people list"
                print self._peopleList
                distanceList=[]
                for i in range (len(self._peopleList)):
                    # get the distance from al the visible poeple
                    distance = self._memProxy.getData("PeoplePerception/Person/" + str(self._peopleList[i]) + "/Distance")
                    distanceList.append(distance)

                print "dit is distance list"
                print distanceList

                for j in range (len(distanceList)):
                    #phytagorean theorie to know the unknow distance

                    try: distanceC=distanceList[(j+1)]
                    except:distanceC=distanceList[j]

                    distanceA=distanceList[j]
                    distanceB=distanceC**2-distanceA**2
                    if ((distanceB**0,5) <= 1.5):
                        print(" je staat te dichtbij")
                        self._mirai.textToSpeech.say("Houden jullie rekening met de annderhalve meter")
