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
        threading.Thread(target=self.startFaceDetection).start()


        # Get the services

    def processFaceDetection(self):

        while self.faceDetectionStarted:
            self.subscriber = self._memProxy.subscriber("FaceDetected")
            self.subscriber.signal.connect(self.on_human_tracked)

    def on_human_tracked(self, value):
        if value == []:  # empty value when the face disappears
            self._gotFace = False
        elif not self._gotFace:  # only speak the first time a face appears
            self._gotFace = True
            print "I saw a face!"




    def startFaceDetection(self):
        #self._proxy.setTrackingEnabled(False)
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

