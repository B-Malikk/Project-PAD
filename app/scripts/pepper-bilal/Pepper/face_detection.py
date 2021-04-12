
class FaceDetection:
    session = face_detection_service = memory_service = None

    def __init__(self, session):
        self.session = session
        self.face_detection_service = self.session.service("ALFaceDetection")
        self.memory_service = self.session.service("ALMemory")


    def start_tracking(self):
        self.face_detection_service.enableTracking(True)


    def stop_tracking(self):
        self.face_detection_service.enableTracking(False)

