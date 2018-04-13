from geometric_utils import distance_from_point_to_rectangle


class Thing:
    def __init__(self, name, width, height, x, y, can_stay_on_carpet):
        self.name = name
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.can_stay_on_carpet = can_stay_on_carpet

    def move(self, x, y):
        self.x += x
        self.y += y

    def calculate_distance_from_point(self, point):
        return distance_from_point_to_rectangle(point, self.coordinates)

    @property
    def x_min(self):
        return self.x - self.width

    @property
    def y_min(self):
        return self.y - self.height

    @property
    def x_max(self):
        return self.x + self.width

    @property
    def y_max(self):
        return self.y + self.height

    @property
    def coordinates(self):
        return [self.x_min, self.y_min, self.x_max, self.y_max]
