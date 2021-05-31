# BasicAwareness

## What is does
ALBasicAwareness is a simple way to make the robot establish and keep eye contact with people.

## Methods
###__init__(*self*, *mirai*)
This method initialises all the attributes of the Conversation class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *mirai* - The main class Mirai. 

###__setBA__(*self*, *bool*)
This method enables or disables basic awareness.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *bool* - True to enable it, false to disable it.


###__setEnagement__(*self*, *mode*)
This method sets the engagement mode.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *mode* - a method that allows the engagement mode a wider range of behaviors such as "Unengaged", "FullyEngaged" and "SemiEngaged".

###__pausAwareness__(*self*)
Manually pauses ALBasicAwareness.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 

###__resumeAwareness__(*self*)
Manually resumes ALBasicAwareness.

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 


