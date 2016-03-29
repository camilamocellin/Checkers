class Position(object):

    def __init__(self):
        self.occupation = []

        self.position = (3,3)

        def get_near(self):
            return self.near

        def set_near(self):
            #will be added some verifications before this
            self.near = [
                (self.position[0] - 1, self.position[1] - 1),
                (self.position[0] - 1, self.position[1] + 1),
                (self.position[0] + 1, self.position[1] - 1),
                (self.position[0] + 1, self.position[1] + 1),
            ]





    def is_occupied(self):
        if self.occupation:
            return True
        return False

