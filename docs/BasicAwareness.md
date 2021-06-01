# BasicAwareness

## What is does
ALBasicAwareness is a simple way to make the robot establish and keep eye contact with people.

## Methods
### \_\_init\_\_(*self*, *mirai*)
This method initialises all the attributes of the BasicAwareness class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *mirai* - The main class Mirai. 

### setBA(*self*, *bool*)
This method enables or disables basic awareness.

__Parameters__
- *bool* - True to enable it, false to disable it.


### setEnagement(*self*, *mode*)
This method sets the engagement mode.

__Parameters__
- *mode* - a method that allows the engagement mode a wider range of behaviors such as "Unengaged", "FullyEngaged" and "SemiEngaged".

### pausAwareness(*self*)
Manually pauses ALBasicAwareness.


### resumeAwareness(*self*)
Manually resumes ALBasicAwareness.



