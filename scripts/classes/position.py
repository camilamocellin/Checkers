class Position(object):

    def __init__(self, localization, color):
        self.occupation = []
        self.localization = (localization[0], localization[1])
        self.color = color

        def get_near(self):
            self.set_near()
            return self.near

        def set_near(self):

            base = [
                (self.localization[0] - 1, self.localization[1] - 1),
                (self.localization[0] - 1, self.localization[1] + 1),
                (self.localization[0] + 1, self.localization[1] - 1),
                (self.localization[0] + 1, self.localization[1] + 1)
            ]

            if (self.localization[0] == 8):
                self.near = [base[0], base[1]]

            elif (self.localization[0] == 1):
                self.near = [base[2], base[3]]

            elif (self.localization[1] == 8):
                self.near = [base[0], base[2]]

            elif (self.localization == 1):
                self.near = [base[3], base[1]]

            elif (self.localization[0] == 1 and self.localization[1] == 1):
                self.near = [base[3]]

            elif (self.localization[0] == 8 and self.localization[1] == 1):
                self.near = [base[1]]

            elif (self.localization[0] == 1 and self.localization[1] == 8):
                self.near = [base[2]]

            elif (self.localization[0] == 8 and self.localization[1] == 8):
                self.near = [base[0]]

            else:
                self.near = [base[0], base[1], base[2], base[3]]

    def is_occupied(self):
        if (self.occupation):
            return True
        return False

    def insert_piece(self, piece):
        self.piece = piece

    def delete_piece(self):
        self.piece = []

    def __str__(self):
        return "Line: %d | Column: %d | Ocupation: %s | Color: %s" % (self.localization[0], self.localization[1], self.occupation, self.color)