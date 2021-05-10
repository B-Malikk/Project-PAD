import time
import threading

class FaceDetection(object):


    def __init__(self, mirai):
        self._proxy = mirai.getProxy('ALSpeechRecognition')
        self._peopleProxy = mirai.getProxy('ALPeoplePerception')
        self._memProxy = mirai.getProxy('ALMemory')
        self._faceDetectionStarted=False
        self._faceId = None
        self._distance = None
        self._gotFace = False
        # Get the services

    def processFaceDetection(self):

        while self.faceDetectionStarted:
            self._memProxy.subscribeToEvent('FaceDetected', 'FaceDetection', 'setFaceInfo')



    def startFaceDetection(self):
        self._proxy.setTrackingEnabled(False)
        # Subscribe to the ALFaceDetection proxy
        # This means that the module will write in ALMemory with
        # the given period 500
        self._proxy.subscribe("Test_Face", 500, 0.0)
        self.faceDetectionStarted = True
        threading.Thread(target=self.processFaceDetection).start()

    def setFaceInfo(self):
        return self._gotFace

    def stop_detection(self):
        self.face_detection_started = False

