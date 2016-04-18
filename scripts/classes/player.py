class Player(object):

    def __init__(self, number):
        self.pieces = []
        self.number = number

    def __str__(self):
        return "Player %d" % self.number