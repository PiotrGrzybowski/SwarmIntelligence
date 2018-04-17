import numpy as np
import itertools

from geometric_utils import circle_field, are_things_in_collision


class Benchmark:
    def evaluate(self):
        raise NotImplementedError()

    def evaluate_solution(self, solution):
        raise NotImplementedError()

    def is_solution_in_domain(self, solution):
        raise NotImplementedError()

    def comparator(self, solution1, solution2):
        raise NotImplementedError()


class Room(Benchmark):
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

    def evaluate(self):
        return circle_field(self.get_max_carpet_radius())

    def evaluate_solution(self, solution):
        self.set_thing_positions(solution)
        return self.evaluate()

    def is_solution_in_domain(self, solution):
        self.set_thing_positions(solution)
        return self.satisfy_constraints()

    def comparator(self, solution1, solution2):
        return self.evaluate_solution(solution1) > self.evaluate_solution(solution2)

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
        return np.min(self.distance_from_center_to_things())

    def satisfy_constraints(self):
        return self.all_things_in_room_range() and not self.is_door_stacked() and not self.is_window_stacked() and not self.exists_overlapping()


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
