from Pepper import connect
from Pepper import dialog
from Pepper import text_speech
from Pepper import face_detection



if __name__ == "__main__":
    topic_content = ('topic: ~topic2()\n'
                       'language: enu\n'
                       'u: (test) Kan ik je ergens mee helpen.\n'
                       'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) .\n'
                       'u: (test) zeg het eens.\n'
                       'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                       'u2: ([lokaal kamer ]) pak de linker lift .\n'
                       'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')

    ip = "127.0.0.1"
    port = 9559

    pepper = connect.Connect(ip,port)
    session = pepper.make_connection()

    #get services en geef de session mee
    tts=text_speech.TextToSpeech(session)
    tts.say("tesssssssssssssssssssssssssssssssssst")
    tts.say("tesssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
    tts.say("halooooooooooooooooooooooooooooooooooooo")
    print("start")


    #fd=face_detection.FaceDetection(session)
    dialog=dialog.Dialog(session)
    print topic_content

    #dialog.stop_dialog()
    dialog.start_dialog("English",topic_content)