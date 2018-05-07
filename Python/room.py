import numpy as np
import itertools

import yaml

from Python.geometric_utils import are_things_in_collision
from Python.thing import Thing
from benchmarks.benchmark import Benchmark


class Room(Benchmark):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.things = []
        self.shapes = []
        self.center = (0, 0)
        # self.doors = []
        # self.windows = []

    def add_door(self, door):
        pass

    def add_window(self, window):
        pass

    def add_thing(self, thing):
        self.things.append(thing)

    def evaluate(self, *args):
        self.set_thing_positions(args)
        return self.get_max_carpet_radius()

    def find_best_solution(self, solutions):
        pass

    def process_borders(self, agents, low, high):
        return agents

    def is_solution_in_domain(self, solution):
        self.set_thing_positions(solution)
        return self.satisfy_constraints()

    def distance_from_center_to_things(self):
        return [thing.calculate_distance_from_point(self.center) for thing in self.things if not thing.can_stay_on_carpet]

    def is_window_stacked(self):
        return False

    def is_door_stacked(self):
        return False

    def set_thing_positions(self, positions):
        for i in range(len(self.things)):
            self.things[i].set_position(positions[2 * i], positions[2 * i + 1])

    def is_thing_in_room_range(self, thing):
        return thing.x_min >= self.x_min and thing.x_max <= self.x_max and \
               thing.y_min >= self.y_min and thing.y_max <= self.y_max

    def all_things_in_room_range(self):
        return all([self.is_thing_in_room_range(thing) for thing in self.things])

    def exists_overlapping(self):
        return any(are_things_in_collision(*pair) for pair in list(itertools.combinations(self.things, 2)))

    def get_max_carpet_radius(self):
        return np.min([self.maximum_carpet_in_empty_room(), self.maximum_carpet_with_things()])

    def satisfy_constraints(self):
        return self.all_things_in_room_range() and not self.is_door_stacked() and not self.is_window_stacked() and not self.exists_overlapping()

    def maximum_carpet_in_empty_room(self):
        return np.min([self.width, self.height]) // 2

    def maximum_carpet_with_things(self):
        return np.min(self.distance_from_center_to_things())

    @property
    def dimension(self):
        return 2 * len(self.things)

    @property
    def variables(self):
        return list(itertools.chain.from_iterable([thing.x, thing.y] for thing in self.things))

    @property
    def x_min(self):
        return self.center[0] - self.width // 2

    @property
    def y_min(self):
        return self.center[1] - self.height // 2

    @property
    def x_max(self):
        return self.center[0] + self.width // 2

    @property
    def y_max(self):
        return self.center[1] + self.height // 2

    def load_from_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
            self.things = [Thing(**v) for v in data.values()]
