import threading

from mirai._mirai import Mirai

mirai = Mirai("mirai.robot.hva-robots.nl", 9559)
mirai.textToSpeech.say("kaas")