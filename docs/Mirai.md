# Mirai

## What it does
The Mirai class is the main class for the Mirai (Pepper) robot, and it contains all parts, such as Animation or
PeoplePerception. It automatically connects to the physical robot on its creation.

## Methods

### \_\_init\_\_(*host*, *port*, *virtualRobot=False*)  
The method that initialises all other parts of the robot. Services like TextToSpeech become part of this object,
so they can be called from anywhere.

Example:
```
mirai = Mirai("192.168.1.11", 9559)
mirai.textToSpeech.say("This is Mirai")
```
 
__Parameters__
- *host* - a string that contains an ip address or hostname (e.g. "mirai.robot.com")
- *port* - an integer that specifies the port to connect to

### getProxy(*name*)  
This method returns the ALProxy object of a NAOqi service, such as ALMotion. Please refer to the
[NAOqi documentation](http://doc.aldebaran.com/2-5/naoqi/index.html) for their methods.

An Exception will be raised when the service cannot be found.
 
__Parameters__
- *name* - The name of the proxy to return, such as ALTextToSpeech

### mqttPublish(*topic*, *message*)
Publishes a message to the MQTT broker with specified topic and message. The topic will be prefixed with "Mirai/".
This is intended to be used as an easy way to publish events without having to use a more extensive MQTT class.
 
__Parameters__
- *topic* - The topic name (a string) to be prefixed with "Mirai/".
- *message* - The message to publish, can be an empty string but is a required parameter
