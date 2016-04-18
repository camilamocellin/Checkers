class Track(object):

    def __init__(self, start, destiny):
        self.start = (start.localization[0], start.localization[1])
        self.destiny = (destiny.localization[0], destiny.localization[1])
        self.track_list = []
        self.set_track_list()

    def set_track_list(self):
        if self.start[0] < self.destiny[0]:
            if self.start[1] < self.destiny[1]:
                x_step = 1
                y_step = 1
            else:
                x_step = 1
                y_step = -1
        else:
            if self.start[1] < self.destiny[1]:
                x_step = -1
                y_step = 1
            else:
                x_step = -1
                y_step = -1
        for x in range(self.start[0], self.destiny[0] + 1, x_step):
            for y in range(self.start[1], self.destiny[1] + 1, y_step):
                self.track_list.append(x,y)

    def get_track(self):
        return track.track_list

    def __str__(self):
        string = 'Track \n'
        for item in self.track_list:
            string += item + " "
        return string