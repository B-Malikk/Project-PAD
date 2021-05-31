# BasicAwareness

## What is does
ALBasicAwareness is a simple way to make the robot establish and keep eye contact with people.

## Methods
### \_\_init\_\_(*self*, *mirai*)
This method initialises all the attributes of the Conversation class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *mirai* - The main class Mirai. 

### setBA(*self*, *bool*)
This method enables or disables basic awareness.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *bool* - True to enable it, false to disable it.


### setEnagement(*self*, *mode*)
This method sets the engagement mode.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *mode* - a method that allows the engagement mode a wider range of behaviors such as "Unengaged", "FullyEngaged" and "SemiEngaged".

### pausAwareness(*self*)
Manually pauses ALBasicAwareness.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 

### resumeAwareness(*self*)
Manually resumes ALBasicAwareness.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 


