import numpy as np
import itertools
import math

import yaml

from Python.geometric_utils import are_things_in_collision, thing_collision_pairs, collision_penalty
from Python.thing import Thing
from benchmarks.benchmark import Benchmark


class Room(Benchmark):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.things = []
        self.shapes = []
        self.center = (0, 0)
        self.window = self.add_window()
        self.door = self.add_door()
        self.min_distance_from_window = 50

    def add_thing(self, thing):
        self.things.append(thing)

    def evaluate(self, *args):
        self.set_thing_positions(args)
        penalty = self.total_penalty()
        return self.get_max_carpet_radius() - penalty

    def find_best_solution(self, solutions):
        return solutions[np.array([self.evaluate(*x.tolist()) for x in solutions]).argmax()]

    def process_borders(self, agents, low, high):
        return agents

    def summary_solutions(self, solutions):
        best = []
        mean = []
        for iteration_solution in solutions:
            bp = []
            for sol in iteration_solution:
                self.set_thing_positions(sol)
                bp.append(self.get_max_carpet_radius())

            best_solution = self.find_best_solution(iteration_solution)
            self.set_thing_positions(best_solution)
            # self.set_thing_positions(solution.tolist())
            best.append(self.get_max_carpet_radius())
            mean.append(np.mean(bp))
        return mean

    def distance_from_center_to_things(self):
        return [thing.calculate_distance_from_point(self.center) for thing in self.things if
                not thing.can_stay_on_carpet]

    def set_thing_positions(self, positions):
        for i in range(len(self.things)):
            self.things[i].set_position(positions[2 * i], positions[2 * i + 1])

    def is_thing_in_room_range(self, thing):
        return thing.x_min >= self.x_min and thing.x_max <= self.x_max and \
               thing.y_min >= self.y_min and thing.y_max <= self.y_max

    def is_angle_good(self, tv, couch):
        return math.fabs(tv.x - couch.x) < math.sqrt((tv.x - couch.x)**2 + (tv.y - couch.y)**2)/2

    def all_things_in_room_range(self):
        return all([self.is_thing_in_room_range(thing) for thing in self.things])

    def exists_overlapping(self):
        return any(are_things_in_collision(*pair) for pair in list(itertools.combinations(self.things, 2)))

    def get_max_carpet_radius(self):
        return np.min([self.maximum_carpet_in_empty_room(), self.maximum_carpet_with_things()])


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

    def is_maximising(self):
        return True

    def is_solution_better_than_global_solution(self, solution, global_solution):
        return self.evaluate(*solution) > self.evaluate(*global_solution)

    def load_from_yml(self, path):
        with open(path) as f:
            data = yaml.safe_load(f)
            self.things = [Thing(**v) for v in data.values()]

    def left_border_penalty(self, thing):
        return np.max([self.x_min - thing.x_min, 0])

    def right_border_penalty(self, thing):
        return np.max([thing.x_max - self.x_max, 0])

    def top_border_penalty(self, thing):
        return np.max([thing.y_max - self.y_max, 0])

    def bottom_border_penalty(self, thing):
        return np.max([self.y_min - thing.y_min, 0])

    def border_penalty(self, thing):
        return np.sqrt(np.power(self.left_border_penalty(thing), 2) +
                       np.power(self.right_border_penalty(thing), 2) +
                       np.power(self.top_border_penalty(thing), 2) +
                       np.power(self.bottom_border_penalty(thing), 2))

    def total_border_penalty(self):
        return np.sum([self.border_penalty(thing) for thing in self.things]) * 2

    def total_collision_penalty(self):
        return np.sum([collision_penalty(*pair) for pair in thing_collision_pairs(self.things)])

    def total_penalty(self):
        return self.total_border_penalty() + self.total_collision_penalty() + self.total_window_penalty() \
               + self.total_door_penalty() + self.penalty_for_tv_angle()

    def add_window(self):
        return Thing('Door', 60, 5, False, x=0, y=self.y_max)

    def add_door(self):
        return Thing('Window', 5, 60, False, x=self.x_max, y=0)

    def is_thing_on_window(self, thing):
        return self.window.x_min < thing.x_min < self.window.x_max or self.window.x_min < thing.x_max < self.window.x_max or self.window.x_min < thing.x < self.window.x_max

    def is_thing_on_door(self, thing):
        return self.door.y_min < thing.y_min < self.door.y_max or self.door.y_min < thing.y_max < self.door.y_max or self.door.y_min < thing.y < self.door.y_max

    def penalty_for_thing_on_window(self, thing):
        return np.max([self.min_distance_from_window - (self.y_max - thing.y_max), 0])

    def penalty_for_thing_on_door(self, thing):
        return np.max([self.min_distance_from_window - (self.x_max - thing.x_max), 0])

    def penalty_for_tv_angle(self):
        tv = [thing for thing in self.things if thing.name == 'TV'][0]
        couch = [thing for thing in self.things if thing.name == 'Couch'][0]
        min_distance = 150
        distance_penalty = min(0, (math.sqrt((tv.x - couch.x)**2 + (tv.y - couch.y)**2) - min_distance))*(-1)
        return distance_penalty if self.is_angle_good(tv, couch) else 100 + distance_penalty

    def total_window_penalty(self):
        return np.sum([self.penalty_for_thing_on_window(thing)*5 for thing in self.things if self.is_thing_on_window(thing)])

    def total_door_penalty(self):
        return np.sum([self.penalty_for_thing_on_door(thing) for thing in self.things if self.is_thing_on_door(thing)])
