#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Using ALDialog Methods"""

import qi
import argparse
import sys


def main(session):
    """
    This example uses ALDialog methods.
    It's a short dialog session with two topics.
    """
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")
    ALDialog.setLanguage("Dutch")

    # writing topics' qichat code as text strings (end-of-line characters are important!)
    topic_content_1 = ('topic: ~example_topic_content()\n'
                       'language: dun\n'
                       'concept:(Help) [help vraag]\n'
                       # 'u: (I [want "would like"] {some} _~food) Sure! You must really like $1 .\n'
                       'u: ([Ik heb hulp nodig. "Kan je me helpen?"]) Waar kan ik je mee helpen?\n'
                       'u: (Mijn pasje [werkt "doet het"] niet) Voor problemen met je pasje kan je terecht bij de '
                       'balie\n '
                       'u: (Waar is de balie?) Welkom leerling, de balie is aan de linker kant.\n'
                       'u: (Hoe gaat het?) Gaat je niks aan\n'
                       'u: ([Waar "Hoe"] kan ik mijn lokaal vinden) Op mijn tablet kan je de route vinden naar elk '
                       'lokaal.\n '
                       'u: (Waar kan ik eten [halen? "kopen?"]) Achter mij is een kantine waar eten verkocht wordt.\n'
                       'u: (Goede middag) Goede middag, veel succes tijdens je les!\n'
                       'u: ([e:FrontTactilTouched e:MiddleTactilTouched e:RearTactilTouched]) You touched my head!\n')

    topic_content_2 = ('topic: ~dummy_topic()\n'
                       'language: dun\n'
                       'proposal: kan ik je ergens mee helpen\n'
                       'u:(test) [a b "c d" "e f g"]\n')

    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content_1)
    topic_name_2 = ALDialog.loadTopicContent(topic_content_2)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)
    ALDialog.activateTopic(topic_name_2)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')

    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')

        # Deactivating all topics
        ALDialog.deactivateTopic(topic_name_1)
        ALDialog.deactivateTopic(topic_name_2)

        # now that the dialog engine is stopped and there are no more activated topics,
        # we can unload all topics and free the associated memory
        ALDialog.unloadTopic(topic_name_1)
        ALDialog.unloadTopic(topic_name_2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="mirai.robot.hva-robots.nl",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the "
                             "default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    main(session)
