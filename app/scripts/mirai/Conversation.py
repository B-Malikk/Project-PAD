
class Dialog(object):
    """Base motion class. Contains all motion related things (body parts, joints, movement, etc)."""
    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: dun\n'
                       'concept:(Help) [help vraag]\n'
                       'u: ([Ik heb hulp nodig. "Kan je me helpen?"]) Waar kan ik je mee helpen?\n'
                       'u: (Mijn pasje [werkt "doet het"] niet) Voor problemen met je pasje kan je terecht bij de '
                       'balie\n '
                       'u: (Waar is de balie?) Welkom leerling, de balie is aan de linker kant.\n'
                       'u: (Hoe gaat het?) Gaat je niks aan\n'
                       'u: ([Waar "Hoe"] kan ik mijn lokaal vinden) Op mijn tablet kan je de route vinden naar elk '
                       'lokaal.\n '
                       'u: (Waar kan ik eten [halen? "kopen?"]) Achter mij is een kantine waar eten verkocht wordt.\n'
                       'u: (Goede middag) Goede middag, veel succes tijdens je les!\n'
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) You touched my head!\n')

    def __init__(self, mirai):
        self._proxy = mirai.getProxy("ALDialog")
        self._topicName = None
        self._dialogStarted = False

    def activateTopic(self, topiccontent, language):
        self._proxy.loadTopicContent(topiccontent)
        self._proxy.activateTopic(topiccontent)
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