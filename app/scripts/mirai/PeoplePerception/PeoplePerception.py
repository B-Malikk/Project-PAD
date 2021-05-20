import threading
import time
import math


class PeoplePerception(object):

    def __init__(self, mirai):
        self._mirai = mirai
        self._proxy = mirai.getProxy('ALPeoplePerception')
        self._memProxy = mirai.getProxy('ALMemory')
        self._peopleList = []
        self.newPersonDetected = False
        self.newPersonID = None
        self.startPeopleDetection()
        self.peopleData = {}

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


        self.subscriber1=self._memProxy.subscriber('PeoplePerception/PeopleDetected')
        self.subscriber1.signal.connect(self.peopleDetected)

        # give callback when event rises
        #self._memProxy.subscribeToEvent('PeoplePerception/JustLeft', 'this', 'leftCallback')
        #self.subscriber1=self._memProxy.subscriber('PeoplePerception/JustLeft')
        #self.subscriber1.signal.connect(self.leftCallback)
        threading.Thread(target=self.procesPeople).start()

    def peopleDetected(self, data):
        allData=data
        personData_i = allData[1][0]
        personData_ID = personData_i[0]
        personData_YawAngle = personData_i[3]
        print personData_ID
        print personData_YawAngle
        self.peopleData.update({personData_ID : personData_YawAngle})



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
                print "dit is people list"
                print self._peopleList
                distanceList=[]
                angleList=[]
                for person in self._peopleList:
                    angleList = self.peopleData.get(person)
                    # get the distance from al the visible poeple
                    try:
                        distance = self._memProxy.getData("PeoplePerception/Person/" + str(person) + "/Distance")
                        distanceList.append(distance)
                    except:
                        pass

                for i in range(len(self._peopleList)):
                    angle=(angleList[i]-angleList[i+1])
                    lenghtA=distanceList[i]
                    lenghtB=distanceList[i+1]
                    distance=math.sqrt(lenghtA**2+lenghtB**2-2*lenghtA*lenghtB*math.cos(angle))
                    if distance<=1.5:
                        print(" je staat te dichtbij")
                        self._mirai.textToSpeech.say("Houden jullie rekening met de annderhalve meter")
