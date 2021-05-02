from MQTT import MQTTListenerBaseClass
from peewee import *
from playhouse.db_url import connect
from datetime import datetime

mydb = connect("mysql://visserb24:6Cn328HQUSNPsp@oege.ie.hva.nl/zvisserb24")


class BaseModel(Model):
    class Meta:
        database = mydb


# Defines table 'User'
class User(BaseModel):
    id = AutoField(primary_key=True)
    nummer = CharField()
    inklokken = BooleanField()
    tijd = DateTimeField()

    class Meta:
        db_table = 'User'


mydb.create_tables([User, ])


class MQTTCardReader(MQTTListenerBaseClass):
    topic = 'Mirai/card/#'

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == 'Mirai/card/scan':
            user, created = User.get_or_create(nummer=msg.payload)
            user.inklokken = True if user.inklokken == False else False
            user.tijd = datetime.utcnow()
            user.save()

            if self.mirai:
                if user.inklokken == True:
                    self.mirai.textToSpeech.say("Welkom.")
                else:
                    self.mirai.textToSpeech.say("Tot ziens!")
        if msg.topic == 'Mirai/card/error':
            if self.mirai:
                self.mirai.textToSpeech.say("Probeer het nog eens.")


# reader = MQTTCardReader(None)
# reader.on_scan()
class_instantie = MQTTCardReader(None)
class_instantie.on_event()
