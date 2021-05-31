# Conversation

## What it does
The Conversation class is the class that contains all the parts for the dialog function. This class can be used to 
activate and deactivate the dialog function. 

## Methods 
###__init__(*self*, *mirai*)

This method initialises all the attributes of the Conversation class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *mirai* - the main class Mirai. 

###activateTopic(*self*, *topicContent*, *language*)
This method activates the dialog function when called. The method will set the language chosen by the user, load
the topic content, activate the topic name and subscribe to the topic.  

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *topicContent* - a variable which contains the dialog, written by the user.
- *language* - a string that specifies the language that will be used. 

###deactivateTopic(*self*, *topicContent*)
This method deactivates the dialog function when called. The method will unsubscribe to the topic, deactivate the topic
and unload the topic. It is important to unload the topic when changing the topic content to prevent any errors
from occurring. If an error pops up it can be solved by running the unloadTopic command.  

__Parameters__
- *self* - a method that can be used to access the attributes that are initialised. 
- *topicContent* - a variable which contains the dialog, written by the user.
- *language* - a string that specifies the language that will be used.