# Motion

## What is does
The ALMotion module provides methods which facilitate making the robot move.

## Methods
### \_\_init\_\_(*mirai*)
Initialises all the attributes of the posture class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *mirai* - The main class Mirai 

### apply(*self.name*, *speed*)
Makes the robot go to the predefined posture asked in parameter. It is possible to modify the speed of the move. 
The move is “intelligent”: it will start from beginning posture of the robot, and choose all the steps to reach 
the asked posture.

__Parameters__
- *self.name* - Name of the predefined posture to be reached
- *speed* - Relative speed between 0.0 and 1.0 base code of this project is set to 1.0

### StandInit(*Posture*)
Predefined posture class to make the robot stand up straight.

### StandZero(*Posture*)
Predefined posture class to make robot stand straight with arms forward.

### Crouch(*Posture*)
Predefined posture class to make robot slump with arms along its body.


