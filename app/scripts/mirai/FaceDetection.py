import time

class FaceDetection(object):


    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALSpeechRecognition')
        self._peopleProxy = mirai.getProxy('ALPeoplePerception')
        self._memProxy = mirai.getProxy('ALMemory')
        self._faceDetectionStarted=False
        self._faceId = None
        self._distance = None
        # Get the services

    def processFaceDetection(self):


        while self.faceDetectionStarted:

            faceInfoArray = self._memProxy.getData("FaceDetected", 0)
            print (faceInfoArray)


            # Check whether we got a valid output: a list with two fields(facedetected.)
            if ( faceInfoArray and isinstance(faceInfoArray, list) and len(faceInfoArray) == 2):

                self._faceId = faceInfoArray[1][0][1][0]
                print (self._faceId)
                #save the distance from the current face
                self._distance = self._memProxy.getData("PeoplePerception/Person/" + str(self._faceId) + "/Distance")
                print (self._distance)
                return self._distance



    def startFaceDetection(self):
        self._proxy.setTrackingEnabled(False)
        # Subscribe to the ALFaceDetection proxy
        # This means that the module will write in ALMemory with
        # the given period 500
        self._proxy.subscribe("Test_Face", 500, 0.0)
        self.faceDetectionStarted = True
        self.processFaceDetection()

    def stop_detection(self):
        self.face_detection_started = False

