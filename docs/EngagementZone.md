# EngagementZone

## What it does
The class EngagementZone allows you to classify zones to detect people and/or movements using their position in space 
of the Mirai <pepper>


## How does it work
The engagement zones are defined by the following 
 
Zone1: nearest zone  
Zone2: farther zone  
Angle: whole angle  

<img src="https://gitlab.fdmci.hva.nl/balalib/images/-/raw/master/engage.png" width="200"><br>



When someone is in one of the zones the memory event is raised  
and you can now when some one entersthe zone or leaves the zone 




## Method list


#### setFirstLimit (*parameter1*, *parameter2*)
Sets the value of zone 1 and the angle

__Parameters__
- *parameter1* - (int) distance in meter
- *parameter2* - (int) angle in degrees between 0-180


#### setSecondLimit (*parameter1*, *parameter2*)
Sets the value of zone 2 and the angle

__Parameters__
- *parameter1* - (int) distance in meter
- *parameter2* - (int) angle in degrees between 0-180


#### getFirstLimit()
Returns the value of zone 1 in meters


#### getSecondLimit()
Returns the value of zone 2 in meters  


#### getAngle()
Returns the value of the angle in degrees

#### start()
Start the process of engagement zones

#### processZones()
Start the process of engagement zones does process the event for entering zone 1 
entering zone 2 and when each person leaves.
For each process a calback is created what subscribes to a topic in the MQTT


When someone enters zone 1 each time a message is published with topic EngagementZones/PersonEnteredZone1  

When someone enters zone 2 each time a message is published with topic  
EngagementZones/PersonEnteredZone2  

When someone moves away each time a message is published with topic  
EngagementZones/PersonMovedAway  

You can read the topic with MQTT handleMessage().  



Example:
```
from mirai._mirai import Mirai #import library
vocubulary=['word1','word2', 'sentenced 1'] # list of vocubulary

mirai = Mirai("mirai.robot.hva-robots.nl", 9559) #ip and port

mirai.engagementZone.setFirstLimit(0.7, 90)#set zone 1
mirai.engagementZone.setSecondLimit(1.2,90)#set zone 2
mirai.engagementZone.start()

```
