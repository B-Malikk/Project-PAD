# SpeechRecognition

## What it does
The SpeechRecognition class gives to the Mirai (pepper)<br> 
the ability to recognize predefined words or phrases in several languages.<br>


##How does it work
-Before starting, SpeechRecognition needs to be fed by the list of phrases that should be recognized.<br>
-If something is heard, the element is placed  in the key WordRecognized.<br>


##Method list

#### setVocabulary(parameter1, parameter2)
Sets the list of words/phrases (vocabulary) that should be recognized by the speech recognition engine.<br> 
If word spotting is disabled (default), the engine expects to hear one of the specified words, nothing more, nothing less. <br>
If enabled, the specified words can be pronounced in the middle of a whole sentenced.<br>  

 
__Parameters__
- *parameter1* - List of words that should be recognized
- *parameter2* - Enable wordspotting(True) or disable it (False)


#### setLanguage(parameter)
Sets the language used by the speech recognition system for the current application.


__Parameters__
- *parameter* - Name of one of the available languages Example: ‘Dutch’

#### getLanguage()
Returns the language currently used by the speech recognition system<br>

#### startSpeecheRecognition()
starts the speechRecognition andSubscribes to ALSpeechRecognition.<br>
 This causes the module to start writing information to ALMemory in “WordRecognized”.<br>

#### cleareMemory()
Removes data from “WordRecognized” in ALMemory <br>

#### stop()
Unsubscribes to ALSpeechRecognition.<br>
This causes the module to stop writing information to ALMemory in “WordRecognized”.<br>
 
 
#### recognizeWord()
Returns the specified words that has been recognized<br>
 



Example:
```
from mirai._mirai import Mirai #import library
vocubulary=['word1','word2', 'sentenced 1'] # list of vocubulary

mirai = Mirai("mirai.robot.hva-robots.nl", 9559) #ip and port

mirai.speechRecognition.setLanguage("Dutch")# setlanguage
mirai.speechRecognition.setVocabulary(vocubulary)#set vocubulary
mirai.speechRecognition.startSpeecheRecognition()# start speechRecognition

word=mirai.speechRecognition.recognizeWord()#save recognised word
if word == vocubulary[1]:
    print "word recognised"
    mirai.speechRecognition.stop()# stop speech/recognition
else: print "nothing recognised"
```
