# RobotState

## What it does
The RobotState class contains the (given) current state from the Mirai(pepper).


##How does it work
-	The Robotstate contains the current state by default ‘open’
-	The RobotState can by changed by any given string type



##Method list


#### GetState()
Returns the current state from the robot. By default ‘open’  can be changed by user using setPosture().<br>

#### setState(Parameter)
Sets the state of the mirai to a given string.<br>

__Parameters__
- *parameter* - (string) Name of the state Example: ‘moving’ 

Example:
```
from mirai._mirai import Mirai #import library
vocubulary=['word1','word2', 'sentenced 1'] # list of vocubulary

mirai = Mirai("mirai.robot.hva-robots.nl", 9559) #ip and port

mirai.robotState.setState("moving")# setState to moving
print mirai.robotState.getState("moving")# show the current state

```