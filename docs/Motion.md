# Motion

## What is does
The ALMotion module provides methods which facilitate making the robot move.

## Methods
### \_\_init\_\_(*self*, *mirai*)
This method initialises all the attributes of the Motion class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *mirai* - The main class Mirai

### wakeUp(*self*)
This method is an effect that wakes the robot up. It turns on stiffness and goes to the StandInit predefined posture.

### rest(*self*)
This method is an effect that makes the robot rest. It goes to a posture with its head down and will turn off stiffness after.

### enableArmsMove(*self*)
This method sets the arm motions to disabled during the move process.

### disableArmsMove(*self*)
This method sets the arm motions to enabled during the move process.

### setAngles(*self*, *joints*, *angles*, *fractionMaxSpeed*)
This method sets angles. This is a non-blocking call.

__Parameters__
- *joints* -  The name or names of joints, chains, “Body”, “JointActuators”, “Joints” or “Actuators”
- *angles* - One or more angles in radians
- *fractionMaxSpeed* - The fraction of maximum speed to use
### setStiffnesses(*joints*, *stiffnesses*)
This method sets the stiffness of one or more joints. This is a non-blocking call.

__Parameters__
- *joints* -  The name or names of joints, chains, “Body”, “JointActuators”, “Joints” or “Actuators”
- *stiffnesses* - One or more stiffnesses between zero and one
### enableIdle()
Starts idle posture control on a chain.

### disableIdle()
Stops idle posture control on a chain.

### point()
This method moves the left arm to point to the left where the service desk is located.

### scanner()
This method moves the right arm to allow the person to scan if the scanner is attached to the wrist of the robot.

### scan2()
This method moves the right arm to gesture to the scanner pole.

### hoofd()
This method allows the head of the robot to tilt the head up a little.
