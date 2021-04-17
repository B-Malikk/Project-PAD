
class Dialog:
    session = dialog_service  = None


    def __init__(self,session):
        self.session = session
        # Getting the service ALDialog
        self.dialog_service = self.session.service("ALDialog")

    def set_language(self,language ):
        self.dialog_service.setLanguage(language)


    # Starting the dialog engine - we need to type an  string as the identifier
    def start_dialog(self,language, topic_name):
        self.set_language(language)

        topicName = self.dialog_service.loadTopicContent(topic_name)
        # Activating the loaded topics
        self.dialog_service.activateTopic(topicName)
        print self.dialog_service.getActivatedTopics()
        self.dialog_service.subscribe('dialog')

        raw_input("\nSpeak to the robot using rules from the just loaded .top file. Press Enter when finished:")






    # stopping the dialog engine
    def stop_dialog(self):
        try:self.dialog_service.unsubscribe('dialog')
        except: pass
        # Deactivating all topics
        self.dialog_service.deactivateTopic(self.topic_name)
        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        self.dialog_service.unloadTopic(self.topic_name)

