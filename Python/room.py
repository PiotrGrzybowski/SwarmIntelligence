import numpy as np
import itertools

from geometric_utils import circle_field


class Room:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.things = []
        self.center = (0, 0)
        # self.doors = []
        # self.windows = []

    def add_door(self, door):
        pass

    def add_window(self, window):
        pass

    def add_thing(self, thing):
        self.things.append(thing)

    def calculate_max_carpet(self):
        return circle_field(np.min(self.distance_from_center_to_things()))

    def distance_from_center_to_things(self):
        return [thing.calculate_distance_from_point(self.center) for thing in self.things]

    def variables(self):
        return list(itertools.chain.from_iterable([[thing.x, thing.y] for thing in self.things]))

    def is_window_stacked(self):
        pass

    def is_door_stacked(self):
        pass
