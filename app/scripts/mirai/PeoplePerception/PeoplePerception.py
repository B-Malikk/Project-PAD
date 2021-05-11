import threading


class PeoplePerception(object):

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALPeoplePerception')
        self._memProxy = mirai.getProxy('ALMemory')
        self._peopleList = []
        self._peopleCounter = 0
        self.startPeopleDetection(4, 10)

    def setRange(self, range):
        self._proxy.setMaximumDetectionRange(range)

    def reset(self):
        self._proxy.resetPopulation()
        self._peopleCounter = 0

    def startPeopleDetection(self, range, time):
        self.reset()#reset people population and counter
        self.setRange(range)
        self._proxy.setTimeBeforePersonDisappears(time)
        self._proxy.setTimeBeforeVisiblePersonDisappears(time)

        #give callback when event rises
        self._memProxy.subscribeToEvent('PeoplePerception/JustArrived', 'this', 'arrivedCallback')
        #self.subscriber=self._memProxy.subscribeToEvent('PeoplePerception/JustArrived')
        #self.subscriber.signal.connect(self.arrivedCallback)

        # give callback when event rises
        self._memProxy.subscribeToEvent('PeoplePerception/JustLeft', 'this', 'leftCallback')
        #self.subscriber1=self._memProxy.subscriber('PeoplePerception/JustLeft()')
        #self.subscriber1.signal.connect(self.leftCallback)
        threading.Thread(target=self.procesPeople).start()
        print ("einde def people")

    def arrivedCallback(self):
        self._peopleCounter = +1

    def leftCallback(self):
        self._peopleCounter = -1

    def procesPeople(self):
        print ("in process def")
        #stay looping to check if second boolean is tru or false
        while True:
            #if there are more than 1 person visible run the code
            while (self._peopleCounter >1):
                #save al ID's from visible poeple in an list
                self._peopleList = self._memProxy.getData("PeoplePerception/VisiblePeopleList")
                distanceList=[]
                for i in range (len(self._peopleList)):
                    # get the distance from al the visible poeple
                    distance = self._memProxy.getData("PeoplePerception/Person/" + str(self._peopleList[i]) + "/Distance")
                    distanceList.append(distance)

                for j in range (len(distanceList)):
                    #phytagorean theorie to know the unknow distance

                    try: distanceC=distanceList[(j+1)]
                    except:distanceC=distanceList[j]

                    distanceA=distanceList[j]
                    distanceB=distanceC**2-distanceA**2
                    if ((distanceB**0,5) <= 1.5):
                        print(" je staat te dichtbij")
                        self._mirai.textToSpeech.say("Houden jullie rekening met de annderhalve meter")
