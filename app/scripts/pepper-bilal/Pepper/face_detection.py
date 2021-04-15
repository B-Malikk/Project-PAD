import time
class FaceDetection:
    session = people_perception_service = face_detection_service = memory_service = None
    face_detection_started=False



    def __init__(self, session):
        self.session = session
        # Get the services
        self.people_perception_service = self.session.service("ALPeoplePerception")
        self.memory_service = self.session.service("ALMemory")
        self.face_detection_service = self.session.service("ALFaceDetection")

    def process_face_detection(self):

        while self.face_detection_started:
            face_info_array = self.memory_service.getData("ExtraInfo", 0)
            print face_info_array

            # Check whether we got a valid output: a list with two fields(facedetected.)
            if (face_info_array and isinstance(face_info_array, list) and len(face_info_array) == 2):
                face_id = face_info_array[0]#get the id from the current face
                print face_id
                #save the distance from the current face
                distance = self.memory_service.getData("PeoplePerception/Person/" + str(face_id) + "/Distance")
                return distance



    def start_face_detection(self):
        print "ik ben bij start"
        self.face_detection_service.setTrackingEnabled(False)
        # Subscribe to the ALFaceDetection proxy
        # This means that the module will write in ALMemory with
        # the given period 500
        self.face_detection_service.subscribe("Test_Face", 500, 0.0)
        self.face_detection_started = True
        self.process_face_detection()
        print "ik ben bij einde"

    def stop_detection(self):
        self.face_detection_started = False





