class Piece(object):

    def __init__(self, position, player):
        self.position = position
        self.localization = position.localization
        self.player = player

    def move(self, destiny):
        track = Track(self.position, destiny)

    def __str__(self):
        return "Piece : %s " % self.player
