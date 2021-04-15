from Pepper import connect
from Pepper import dialog
from Pepper import text_speech
from Pepper import face_detection

topic_content_1 = ('topic: ~topic1()\n'
                       'language: enu\n'
                       'u: Kan ik je ergens mee helpen.\n'
                        'u1: ([ja jahoor jawel yes inderdaad wil je me helpen help]) .\n'
                            'u: zeg het eens.\n'
                            'u2: ([pasje mijn pasje kwijt pasje stuk]) ik verwijz je door naar de balie .\n'
                            'u2: ([lokaal kamer ]) pak de linker lift .\n'
                        'u1: ([nee no nope nada hoeft niet doei]) fijne dag nog\n')


if __name__ == "__main__":

    ip = "mirai.robot.hva-robots.nl"
    port = 9559

    pepper = connect.Connect(ip,port)
    session = pepper.make_connection()

    #get services en geef de session mee
    tts=text_speech.TextToSpeech(session)
    fd=face_detection.FaceDetection(session)
    dialog=dialog.Dialog(session)

    dialog.start_dialog("Dutch",topic_content_1)