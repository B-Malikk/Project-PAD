
class Dialog(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""
    topic_content_1 = ('topic: ~topic23()\n'
                       'language: dun\n'
                       'concept:(Help) [help vraag]\n'
                       # 'u: (I [want "would like"] {some} _~food) Sure! You must really like $1 .\n'
                       'u: (kaas) Gaat je niks aan\n'
                       'u: (help mij) Nee\n'
                       'u: (ik ben mijn pasje kwijt) ga naar de balie\n'
                       'u: (Ik weet niet waar mijn lokaal is) Op mijn tablet kan je je lokaal vinden\n'
                       'u: (Waar ben ik) Je bent in het wibauthuis\n')

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALDialog")
        self._topicName = None
        self._dialogStarted = False

    def activateTopic(self, topiccontent, language):
        topicname = self._proxy.loadTopicContent(topiccontent)
        self._proxy.activateTopic(topicname)
        self._proxy.setLanguage(language)
        self._proxy.subscribe('my_dialog_example')

    def deactivateTopic(self, topiccontent):
        try:
            print
        finally:
            # stopping the dialog engine
            self._proxy.unsubscribe('my_dialog_example')

            # Deactivating all topics
            self._proxy.deactivateTopic(topiccontent)

            # now that the dialog engine is stopped and there are no more activated topics,
            # we can unload all topics and free the associated memory
            self._proxy.unloadTopic(topiccontent)
            #mqtt listner back = stop