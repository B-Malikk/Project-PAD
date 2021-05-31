from random import random


class Animation(object):
    """Base class for an animation. Animations have different variants (not all starting from 1) and are part of a group."""
    name = '' # Set automatically by classname
    variants = [1, 2, 3]
    group = 'group'

    def __init__(self, mirai):
        self.proxy = mirai.getProxy("ALAnimationPlayer")
        self.name = self.__class__.__name__

    def run(self, number=0, _async=True):
        try:
            self.proxy.run(self.getPath(number),  _async=_async)
            return True
        except RuntimeError:
            return False

    def getPath(self, number=0):
        if number == 0:
            number = int(random() * len(self.variants))
        return "animations/[posture]/{}/{}_{}".format(self.group, self.name, number)


# Not working unfortunately...
#class BodyTalk(Animation):
#    variants = range(1, 17)
#    group = 'BodyTalk'
#    pass

class Bored(Animation):
    variants = [1]
    group = 'Emotions/Negative'
    pass

class Embarrassed(Animation):
    variants = [1]
    group = 'Emotions/Neutral'
    pass

class Happy(Animation):
    variants = [4]
    group = 'Emotions/Positive'
    pass

class Hysterical(Animation):
    variants = [1]
    group = 'Emotions/Positive'
    pass

class Peaceful(Animation):
    variants = [1]
    group = 'Emotions/Positive'
    pass

class BowShort(Animation):
    variants = [1]
    group = 'Gestures'
    pass

class But(Animation):
    variants = [1]
    group = 'Gestures'
    pass

class CalmDown(Animation):
    variants = [1, 5, 6]
    group = 'Gestures'
    pass

class Choice(Animation):
    variants = [1]
    group = 'Gestures'
    pass

class Desperate(Animation):
    variants = [1, 2, 4, 5]
    group = 'Gestures'
    pass

class Enthusiastic(Animation):
    variants = [4, 5]
    group = 'Gestures'
    pass

class Everything(Animation):
    variants = [1, 2, 3, 4]
    group = 'Gestures'
    pass

class Excited(Animation):
    variants = [1]
    group = 'Gestures'
    pass

class Explain(Animation):
    variants = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
    group = 'Gestures'
    pass

class Far(Animation):
    variants = [1, 2, 3]
    group = 'Gestures'
    pass

class Give(Animation):
    variants = [3, 4, 5, 6]
    group = 'Gestures'
    pass

class Hey(Animation):
    variants = [1, 3, 4, 6]
    group = 'Gestures'
    pass

class IDontKnow(Animation):
    variants = [1, 2, 3]
    group = 'Gestures'
    pass

class Me(Animation):
    variants = [1, 2, 4, 7]
    group = 'Gestures'
    pass

class No(Animation):
    variants = [1, 2, 3, 8, 9]
    group = 'Gestures'
    pass

class Nothing(Animation):
    variants = [2]
    group = 'Gestures'
    pass

class Please(Animation):
    variants = [1]
    group = 'Gestures'
    pass

class ShowFloor(Animation):
    variants = [1, 3, 4]
    group = 'Gestures'
    pass

class ShowSky(Animation):
    variants = [1, 2, 4, 5, 6, 7, 8, 9, 11]
    group = 'Gestures'
    pass

class ShowTablet(Animation):
    variants = [2, 3]
    group = 'Gestures'
    pass

class Thinking(Animation):
    variants = [1, 3, 4, 6, 8]
    group = 'Gestures'
    pass

class Yes(Animation):
    variants = [1, 2, 3]
    group = 'Gestures'
    pass

class YouKnowWhat(Animation):
    variants = [1, 2, 3, 5, 6]
    group = 'Gestures'
    pass

class You(Animation):
    variants = [1, 4]
    group = 'Gestures'
    pass


class Animations(object):
    def __init__(self, mirai):
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
