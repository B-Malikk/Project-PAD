import sys
import qi


class Mirai(object):

    def __init__(self, host, ip):
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + host + ":" + str(ip))
        except RuntimeError:
            print("Can't connect to Naoqi at ip \"" + host + "\" on port " + str(ip))
            sys.exit(1)