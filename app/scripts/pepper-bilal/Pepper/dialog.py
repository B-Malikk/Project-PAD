
class Dialog:
    session = dialog_service= topic_name  = None


    def __init__(self,session):
        self.session = session
        # Getting the service ALDialog
        self.dialog_service = self.session.service("ALDialog")

    def set_language(self,language ):
        self.dialog_service.setLanguage(language)


    # Starting the dialog engine - we need to type an  string as the identifier
    def start_dialog(self,language, topic_name):
        self.set_language(language)
        self.topic_name = self.dialog_service.loadTopicContent(topic_name)
        # Activating the loaded topics
        self.dialog_service.activateTopic(self.topic_name)
        #self.dialog_service.say(self.topic_name)
        print self.dialog_service.getActivatedTopics()
        self.dialog_service.subscribe('dialog')

        try:
            raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
        finally:
            self.stop_dialog(self.topic_name)

        #self.dialog_service.deactivateTopic(topicName)
        #self.dialog_service.unloadTopic(topicName)







    # stopping the dialog engine
    def stop_dialog(self,topic_name):
        # Deactivating all topics
        self.dialog_service.unsubscribe('dialog')
        self.dialog_service.deactivateTopic(topic_name)
        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        self.dialog_service.unloadTopic(topic_name)
        self.dialog_service.unsubscribe('dialog')

