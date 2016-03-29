class Position(object):

    def __init__(self):
        self.occupation = []
        self.near = [
            (self.position[0] - 1, self.position[1] - 1),
            (self.position[0] - 1, self.position[1] + 1),
            (self.position[0] + 1, self.position[1] - 1),
            (self.position[0] + 1, self.position[1] + 1),
        ]
        self.position = (3,3)

        def get_near(self):
            return self.near





    def is_occupied(self):
        if self.occupation:
            return True
        return False

