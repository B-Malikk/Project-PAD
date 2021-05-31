
class Dialog(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALDialog")
        self._topicName = None
        self._dialogStarted = False

    def activateTopic(self, topiccontent, language):
        self._proxy.setLanguage(language)
        topicname = self._proxy.loadTopicContent(topiccontent)
        self._proxy.activateTopic(topicname)
        self._proxy.subscribe('my_dialog_example')

    def deactivateTopic(self, topiccontent):
        try:# stopping the dialog engine
            self._proxy.unsubscribe('my_dialog_example')

            # Deactivating all topics
            self._proxy.deactivateTopic(topiccontent)

            # now that the dialog engine is stopped and there are no more activated topics,
            # we can unload all topics and free the associated memory
            self._proxy.unloadTopic(topiccontent)
            #mqtt listner back = stop
        except: pass
