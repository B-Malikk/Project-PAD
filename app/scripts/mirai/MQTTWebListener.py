from MQTT import MQTTListenerBaseClass
import time


class MQTTWebListener(MQTTListenerBaseClass):
    topic = 'Mirai/web/#'
    topic_content2 = ('topic: ~topic3()\n'
                      'language: enu\n'
                      'proposal: Kan ik je ergens mee helpen\n'
                        'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) waarmee kan ik je helpen .\n'
                        'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                        'u2: ([lokaal kamer klas ]) pak de linker lift .\n'
                        'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if str(msg.payload) == 'pas':
            self.mirai.textToSpeech.say("ik verwijs je door naar de balie.")
        elif str(msg.payload) == 'lokaal':
            self.mirai.textToSpeech.say("vull alleen je lokaal nummer in.")
        elif str(msg.payload) == 'plattegrond':
            self.mirai.textToSpeech.say("je bent nu in het HVA Wibauthuis aan de wibautstraat.")
        elif str(msg.payload) == 'dutch':
            self.mirai.textToSpeech.say("selecteer een probleem of roep het naar mij")

            #self.mirai.dialog.start_dialog("Dutch",self.topic_content2)

        elif str(msg.payload) == 'card':
            self.mirai.textToSpeech.say("I will refer you to the counter.")
        elif str(msg.payload) == 'map':
            self.mirai.textToSpeech.say("you are now in the HVA Wibauthuis on the wibautstraat.")
        elif str(msg.payload) == 'id':
            self.mirai.textToSpeech.say("only enter your classroom number.")
        if str(msg.payload) == 'english':
            self.mirai.textToSpeech.say("select a problem or ask me")
            #self.mirai.ENGP.askForHelp()
