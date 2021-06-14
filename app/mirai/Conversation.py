
class Dialog(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALDialog")
        self._topicName = None
        self._dialogStarted = False

    # Activates the dialog with the chosen topic
    def activateTopic(self, topiccontent, language):
        # sets the spoken language to desired language
        self._proxy.setLanguage(language)
        # Loads the chosen topic and puts it in a variable
        topicname = self._proxy.loadTopicContent(topiccontent)
        # activates chosen topic
        self._proxy.activateTopic(topicname)
        #starts the dialog engine
        self._proxy.subscribe('my_dialog_example')

    # deactivates dialog
    def deactivateTopic(self, topiccontent):
        # Will try to stop the dialog unless an error occurs
        try:# stopping the dialog engine
            self._proxy.unsubscribe('my_dialog_example')

            # Deactivating all topics
            self._proxy.deactivateTopic(topiccontent)

            # now that the dialog engine is stopped and there are no more activated topics,
            # all topics are unloaded and the associated memory is emptied
            self._proxy.unloadTopic(topiccontent)
        except: pass
