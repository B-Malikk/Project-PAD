import qi

class Connect:

    session = ip = port = None

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port


    def make_connection(self):
        self.session = qi.Session()
        self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        return self.session
