import numpy as np

from benchmarks.benchmark import Benchmark


class MathFunction(Benchmark):
    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def dimension(self):
        return 2

    def find_best_solution(self, solutions):
        return solutions[np.array([self.evaluate(*x) for x in solutions]).argmin()]

    def process_borders(self, agents, low, high):
        return np.clip(agents, low, high)

    def is_maximising(self):
        return False

    def is_solution_better_than_global_solution(self, solution, global_solution):
        return self.evaluate(*solution) < self.evaluate(*global_solution)


class BohachevskyFunction(MathFunction):
    def evaluate(self, x, y):
        return x ** 2 + 2 * y ** 2 - 0.3 * np.cos(3 * np.pi * x) - 0.4 * np.cos(4 * np.pi * y) + 0.7


class EasomFunction(MathFunction):
    def evaluate(self, x, y):
        return -np.cos(x) * np.cos(y) * np.exp(-(x - np.pi) ** 2 - (y - np.pi) ** 2)


class Ackley2Function(MathFunction):
    def evaluate(self, x1, x2):
        x = [x1, x2]
        return -np.exp(-np.sqrt(0.5 * sum([i ** 2 for i in x]))) - np.exp(0.5 * sum([np.cos(i) for i in x])) + 1 + np.exp(1)


class HolderTableFunction(MathFunction):
    def evaluate(self, x1, x2):
        return -np.fabs(np.sin(x1) * np.cos(x2) * np.exp(np.fabs(1 - np.sqrt(x1 * x1 + x2 * x2) / np.pi)))
