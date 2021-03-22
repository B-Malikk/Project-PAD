
class FaceDetection:
    session = faceDetectionService = memoryService = None

    def __init__(self, session):
        self.session = session
        self.faceDetectionService = self.session.service("ALFaceDetection")
        self.memoryService = self.session.service("ALMemory")


    def startTrackFace(self):
        self.faceDetectionService.enableTracking(True)


    def stopTrackFace(self):
        self.faceDetectionService.enableTracking(False)

