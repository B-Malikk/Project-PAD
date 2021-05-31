# Animation

## What is does
The ALAnimation module provides methods which facilitate making the robot move.

## Methods
### \_\_init\_\_(*self*, *mirai*)
This method initialises all the attributes of the Animation class. The attributes can later be accessed by using
the self method. 

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *mirai* - The main class Mirai. 

### run(*self*, *number=0*, *_async=True*)
This method starts an animation when called on.

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *number* - Number of the animation
- *_async* - Is set to True this means the request will not wait before continuing to the next line of code.

### getPath(*self*, *number=0*)
This method return a format for the "run" method. 

```
return "animations/[posture]/{}/{}_{}".format(self.group, self.name, number)
```

__Parameters__
- *self* - A method that can be used to access the attributes that are initialised. 
- *number* - Number of the animation
- *self.group* - The name of the group 'path'
- *self.name* - The name of the Class 'path'

###List of all Animations
This is a list of all animations in the class Animations.

```
        self.Embarrassed = Embarrassed(mirai)
        self.Happy = Happy(mirai)
        self.Hysterical = Hysterical(mirai)
        self.Peaceful = Peaceful(mirai)
        self.BowShort = BowShort(mirai)
        self.But = But(mirai)
        self.CalmDown = CalmDown(mirai)
        self.Choice = Choice(mirai)
        self.Desperate = Desperate(mirai)
        self.Enthusiastic = Enthusiastic(mirai)
        self.Everything = Everything(mirai)
        self.Excited = Excited(mirai)
        self.Explain = Explain(mirai)
        self.Far = Far(mirai)
        self.Give = Give(mirai)
        self.Hey = Hey(mirai)
        self.IDontKnow = IDontKnow(mirai)
        self.Me = Me(mirai)
        self.No = No(mirai)
        self.Nothing = Nothing(mirai)
        self.Please = Please(mirai)
        self.ShowFloor = ShowFloor(mirai)
        self.ShowSky = ShowSky(mirai)
        self.ShowTablet = ShowTablet(mirai)
        self.Thinking = Thinking(mirai)
        self.Yes = Yes(mirai)
        self.YouKnowWhat = YouKnowWhat(mirai)
        self.You = You(mirai)
```
