from MQTT import MQTTListenerBaseClass
from peewee import *
from playhouse.db_url import connect

mydb = connect("mysql://visserb24:6Cn328HQUSNPsp@oege.ie.hva.nl/zvisserb24")


class BaseModel(Model):
    class Meta:
        database = mydb
        db_table = 'User'


# Defines table 'User'
class User(BaseModel):
    id = AutoField(primary_key=True)
    nummer = CharField()
    inklokken = BooleanField()
    tijd = TimeField()


class MQTTCardReader(MQTTListenerBaseClass):
    topic = 'Mirai/card/#'

    def on_event(self, msg):
        print(msg.topic + " " + str(msg.payload))
        if msg.topic == 'Mirai/card/scan':
            pass

        ids = []
        for msg.payload in ids:
            if not msg.payload in ids:
                print("not in array yet")
                ids.append(msg.payload)
                User.create(nummer='10')
            else:
                print("already in array")
                ids.remove(msg.payload)
                User.delete().where(User.nummer == '10')
        print(ids)

# reader = MQTTCardReader(None)
# reader.on_scan()
class_instantie = MQTTCardReader(MQTTListenerBaseClass)
class_instantie.on_event()
