from Pepper import connect
from Pepper import dialog
from Pepper import text_speech
from Pepper import Motion
from Pepper import face_detection



if __name__ == "__main__":
    topic_content2 = ('topic: ~topic3()\n'
                       'language: enu\n'
                       'proposal: Kan ik je ergens mee helpen\n'
                       'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) waarmee kan ik je helpen .\n'
                       'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                       'u2: ([lokaal kamer klas ]) pak de linker lift .\n'
                       'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')

    ip = "mirai.robot.hva-robots.nl"
    port = 9559

    pepper = connect.Connect(ip,port)
    session = pepper.make_connection()

    #get services en geef de session mee
    tts=text_speech.TextToSpeech(session)
    motion=Motion.Motion(session)
    tts.say("dag ayman")
    from Pepper import text_speech
    print("start")

    motion.wakeup()


    #fd=face_detection.FaceDetection(session)
    dialog=dialog.Dialog(session)
    #print topic_content2

    #dialog.stop_dialog()
    dialog.start_dialog("English",topic_content2)