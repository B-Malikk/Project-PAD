from MQTT import MQTTListenerBaseClass
from peewee import *
from playhouse.db_url import connect

mydb = connect("mysql://visserb24:6Cn328HQUSNPsp@oege.ie.hva.nl/zvisserb24")


class BaseModel(Model):
    class Meta:
        database = mydb


# Defines table 'User'
class User(BaseModel):
    id = AutoField(primary_key=True)
    nummer = CharField()
    inklokken = BooleanField()
    tijd = TimeField()

    class Meta:
        db_table = 'User'


mydb.create_tables([User, ])


class MQTTCardReader(MQTTListenerBaseClass):
    topic = 'Mirai/card/#'

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == 'Mirai/card/scan':
            pass
        user, created = User.get_or_create(nummer=msg.payload)
        user.inklokken = True if user.inklokken == False else False
        user.save()


# reader = MQTTCardReader(None)
# reader.on_scan()
class_instantie = MQTTCardReader(MQTTListenerBaseClass)
class_instantie.on_event()
