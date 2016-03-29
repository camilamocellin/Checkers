class Track(object):

    def __init__(self, start, destiny):
        self.start = (start.localization[0], start.localization[1])
        self.destiny = (destiny.localization[0], destiny.localization[1])
        self.track_list = []

    def set_track_list(self):
        if start[0] < destiny[0]:
            if start[1] < destiny[1]:
                x_step = 1
                y_step = 1
            else:
                x_step = 1
                y_step = -1
        else:
            if start[1] < destiny[1]:
                x_step = -1
                y_step = 1
            else:
                x_step = -1
                y_step = -1
        for x in range(start[0], destiny[0] + 1, x_step):
            for y in range(start[1], destiny[1] + 1, y_step):
                self.track_list.append(x,y)