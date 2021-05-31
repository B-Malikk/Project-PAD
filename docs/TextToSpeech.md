# TextToSpeech


## What it does


The TextToSpeech class is the class that contains all the parts for the text to speech function. This class can be used to set the language, speed and volume. It can also be used to make Mirai say something and to make Mirai use animations that make her more human like.


## Methods 

###__init__(*self*, *mirai*)

This method initialises all the attributes of the TextToSpeech class. The attributes can later be accessed by using the self method. 
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *mirai* - the main class Mirai. 

###setLanguage(*self*, *language*)

This method sets the language that is chosen by the user. This language is used by Mirai to change the spoken language.
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *language* - a string that specifies the language that will be used. 

###getLanguage(*self*)

This method returns the language that was chosen earlier.   

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 

###setSpeed(*self*, *speed*)

This method sets the speed of the text to speech. The speed can be chosen by changing the integer. 
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *speed* - an integer that specifies the speed that will be used by Mirai. 

###setVolume(*self*, *volume*)

This method sets the volume of the text to speech. The volume can be chosen by changing the integer. 
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *volume* - an integer that specifies the volume that will be used by Mirai.

###say	(*self*, *text*, *language=None*)

This method enables the user to enter a string which Mirai will pronounce. 
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *text* - a string that specifies the text that will be used by Mirai.
- *language* - a string that specifies the language used by Mirai.

###sayAnimated(*self*, *text*, *mode=None*)

This method enables the user to enter a string which Mirai will pronounce and a mode which sets the type of animation that Mirai will use.
__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *text* - a string that specifies the text that will be used by Mirai.
- *mode* - a string that specifies the mode of animation used by Mirai.