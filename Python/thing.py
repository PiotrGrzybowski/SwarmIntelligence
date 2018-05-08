from Python.geometric_utils import distance_from_point_to_rectangle


class Thing:
    def __init__(self, name, width, height, can_stay_on_carpet, x=0, y=0):
        self.y = y
        self.x = x
        self.name = name
        self.width = width
        self.height = height
        self.can_stay_on_carpet = can_stay_on_carpet

    def move(self, x, y):
        self.x += x
        self.y += y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance_from_point(self, point):
        return distance_from_point_to_rectangle(point, self.coordinates)

    @property
    def x_min(self):
        return self.x - self.width / 2

    @property
    def y_min(self):
        return self.y - self.height / 2

    @property
    def x_max(self):
        return self.x + self.width / 2

    @property
    def y_max(self):
        return self.y + self.height / 2

    @property
    def coordinates(self):
        return [self.x_min, self.y_min, self.x_max, self.y_max]

    @property
    def position(self):
        return [self.x, self.y]
