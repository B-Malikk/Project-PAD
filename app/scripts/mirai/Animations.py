from random import random


class Animation(object):
    name = '' # Set automatically by classname
    variants = [1, 2, 3]
    group = 'group'

    def __init__(self, session):
        self.session = session
        self.name = self.__class__.__name__

    def run(self, number=0, _async=False):
        if number == 0:
            number = int(random() * len(self.variants))
        animation_service = self.session.service("ALAnimationPlayer")
        try:
            animation_service.run("animations/[posture]/{}/{}_{}".format(self.group, self.name, number),  _async=_async)
            return True
        except RuntimeError:
            return False

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


def get_all(mirai):
    return {
        #'BodyTalk': BodyTalk(mirai),
        'Embarrassed': Embarrassed(mirai),
        'Happy': Happy(mirai),
        'Hysterical': Hysterical(mirai),
        'Peaceful': Peaceful(mirai),
        'BowShort': BowShort(mirai),
        'But': But(mirai),
        'CalmDown': CalmDown(mirai),
        'Choice': Choice(mirai),
        'Desperate': Desperate(mirai),
        'Enthusiastic': Enthusiastic(mirai),
        'Everything': Everything(mirai),
        'Excited': Excited(mirai),
        'Explain': Explain(mirai),
        'Far': Far(mirai),
        'Give': Give(mirai),
        'Hey': Hey(mirai),
        'IDontKnow': IDontKnow(mirai),
        'Me': Me(mirai),
        'No': No(mirai),
        'Nothing': Nothing(mirai),
        'Please': Please(mirai),
        'ShowFloor': ShowFloor(mirai),
        'ShowSky': ShowSky(mirai),
        'ShowTablet': ShowTablet(mirai),
        'Thinking': Thinking(mirai),
        'Yes': Yes(mirai),
        'YouKnowWhat': YouKnowWhat(mirai),
        'You': You(mirai),
    }
