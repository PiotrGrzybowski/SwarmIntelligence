import numpy as np


class Algorithm:
    def find_best_solution(self, benchmark):
        pass


class PartialSwarmOptimization:
    def __init__(self, benchmark, low, high):
        self.benchmark = benchmark
        self.global_solution = None
        self.partials = None
        self.low = low
        self.high = high

    def find_best_solution(self, partials, iterations):
        self.initialize_partials(partials)
        self.initialize_global_solution()

        for i in range(iterations):
            pass

    def initialize_partials(self, partials):
        self.partials = [Partial(self.benchmark.dimension, self.low, self.high) for _ in range(partials)]

    def initialize_global_solution(self):
        solutions_in_domain = [partial for partial in self.partials if self.benchmark.is_solution_in_domain(partial.solution)]
        self.global_solution = max(solutions_in_domain, key=lambda x: self.benchmark.evaluate_solution(x.solution)).solution

    def update_partial_velocity(self, partial, c1, c2):
        partial.update_velocity(self.global_solution, c1, c2)


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

    def update_velocity(self, global_solution, c1, c2):
        self.velocity += (self.best_solution - self.solution) * c1 * np.random.uniform(0, 1) + (global_solution - self.solution) * c2 * np.random.uniform(0, 1)

    def update_solution(self):
        self.solution += self.velocity