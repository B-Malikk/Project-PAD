
class Face(object):
    id = None

    def __init__(self, data):
        self.id = data[1]


    def getID(self):
        return self.id

    def setID(self,id):
        self.id = id
