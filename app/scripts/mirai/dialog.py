
class Dialog(object):


    def __init__(self,mirai):
        self._dialogService = mirai.getProxy('ALDialog')
        self._topicName = None
        # Getting the service ALDialog

    def set_language(self,language ):
        self._dialogService.setLanguage(language)


    # Starting the dialog engine - we need to type an  string as the identifier
    def start_dialog(self,language, topic_name):
        self.set_language(language)
        self._topicName = self._dialogService.loadTopicContent(topic_name)
        # Activating the loaded topics
        self._dialogService.activateTopic(self._topicName)
        #self.dialog_service.say(self.topic_name)
        print self._dialogService.getActivatedTopics()
        self._dialogService.subscribe('dialog')

        try:
            raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
        finally:
            self.stop_dialog(self._topicName)

        #self.dialog_service.deactivateTopic(topicName)
        #self.dialog_service.unloadTopic(topicName)







    # stopping the dialog engine
    def stop_dialog(self,topic_name):
        # Deactivating all topics
        self._dialogService.unsubscribe('dialog')
        self._dialogService.deactivateTopic(topic_name)
        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        self._dialogService.unloadTopic(topic_name)
        self._dialogService.unsubscribe('dialog')

