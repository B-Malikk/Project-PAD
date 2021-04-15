topic_content_1 = ('topic: ~topic1()\n'
                       'language: enu\n'
                       'u: Kan ik je ergens mee helpen.\n'
                        'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) .\n'
                            'u: zeg het eens.\n'
                            'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                            'u2: ([lokaal kamer ]) pak de linker lift .\n'
                        'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')
class Dialog:
    session = dialog_service = topic_name = None


    def __init__(self,session):
        self.session = session
        # Getting the service ALDialog
        self.dialog_service = self.session.service("ALDialog")

    def set_language(self,language ):
        self.dialog_service.setLanguage(language)


    # Starting the dialog engine - we need to type an  string as the identifier
    def start_dialog(self,language, topic_name):
        self.set_language(language)
        self.dialog_service.subscribe('dialog')
        self.topic_name = self.load_dialog(topic_name)
        self.activate_dialog(self.topic_name)

    def load_dialog(self,name):
        # Loading the topics directly as text strings
        self.dialog_service.loadTopicContent(name)

    def activate_dialog(self,name):
        # Activating the loaded topics
        self.dialog_service.activateTopic(name)



    # stopping the dialog engine
    def stop_dialog(self,):
        self.dialog_service.unsubscribe('dialog')
        self.deactivate_dialog(self.topic_name)
        self.unload_dialog(self.topic_name)


    def unload_dialog(self,name):
        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        self.dialog_service.unloadTopicContent(name)

    def deactivate_dialog(self,name):
        # Deactivating all topics
        self.dialog_service.deactivateTopic(name)


