import numpy as np


class Algorithm:
    def find_best_solution(self, benchmark):
        pass


class PartialSwarmOptimization:
    def __init__(self, benchmark):
        self.benchmark = benchmark
        self.global_solution = None
        self.partials = None

    def find_best_solution(self, partials):
        self.initialize_partials(partials)

    def initialize_partials(self, partials):
        self.partials = [Partial(self.benchmark.dimension, -100, 100) for _ in range(partials)]

    def initialize_global_solution(self):
        pass


class Partial:
    def __init__(self, dimension, low, high):
        self.low = low
        self.high = high
        self.dimension = dimension
        self.solution = self.initialize_solution()
        self.velocity = self.initialize_velocity()
        self.best_solution = self.solution

    def initialize_solution(self):
        return np.random.uniform(self.low, self.high, self.dimension)

    def initialize_velocity(self):
        return np.random.uniform(-np.abs(self.high - self.low), np.abs(self.high - self.low), self.dimension)
