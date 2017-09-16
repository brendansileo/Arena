class ship:

    x_p = 0
    y_p = 0

    x_v = 0
    y_v = 0

    x_a = 0
    y_a = 0

    angle = 0

    def __init__(self, x, y):
        self.x_p = x
        self.y_p = y

    def toString(self):
        return str(self.x_p) + ' ' + str(self.y_p) + ' ' + str(self.angle)
