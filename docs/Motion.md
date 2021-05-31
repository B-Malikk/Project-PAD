# Motion

## What is does
The ALMotion module provides methods which facilitate making the robot move.

## Methods
### \_\_init\_\_(*self*, *mirai*)
This method initialises all the attributes of the Motion class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *mirai* - The main class Mirai. 

### wakeUp(*self*)
This method is an effect that wakes the robot up. It turns on stiffness and goes to the StandInit predefined posture.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
### rest(*self*)
This method is an effect that makes the robot rest. It goes to a posture with its head down and will turn off stiffness after.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
### enableArmsMove(*self*)
This method sets the arm motions to disabled during the move process.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### disableArmsMove(*self*)
This method sets the arm motions to enabled during the move process.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### moveForward(*self*, *meters*)

### moveLeft(*self*, *meters*)

### moveRight(*self*, *meters*)

### moveBack(*self*, *meters*)

### moveTo(*self*, *x*, *y*, *degrees*)

### moveToward(*self*, *velocityX*, *velocityY*, *velocityAxis*)

### rotateAntiClockWise(*self*, *degrees*)

### rotateClockWise(*self*, *degrees*)

### stopMove(*self*)

### setAngles(*self*, *joints*, *angles*, *fractionMaxSpeed*)
This method sets angles. This is a non-blocking call.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *joints* -  The name or names of joints, chains, “Body”, “JointActuators”, “Joints” or “Actuators”.
- *angles* - One or more angles in radians
- *fractionMaxSpeed* - The fraction of maximum speed to use.
### setStiffnesses(*self*, *joints*, *stiffnesses*)
This method sets the stiffness of one or more joints. This is a non-blocking call.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *joints* -  The name or names of joints, chains, “Body”, “JointActuators”, “Joints” or “Actuators”.
- *stiffnesses* - One or more stiffnesses between zero and one.
### enableIdle(*self*)
Starts idle posture control on a chain.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### disableIdle(*self*)
Stops idle posture control on a chain.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### point(*self*)
This method moves the left arm to point to the left where the service desk is located.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### scanner(*self*)
This method moves the right arm to allow the person to scan if the scanner is attached to the wrist of the robot.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### scan2(*self*)
This method moves the right arm to gesture to the scanner pole.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
### hoofd(*self*)
This method allows the head of the robot to tilt the head up a little.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised.
