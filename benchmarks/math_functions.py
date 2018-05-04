import numpy as np

from benchmark import Benchmark


def easom_function(x):
    return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-(x[0] - np.pi) ** 2 - (x[1] - np.pi) ** 2)


def bohachevsky_function(x):
    return x[0] ** 2 + 2 * x[1] ** 2 - 0.3 * np.cos(3 * np.pi * x[0]) - 0.4 * np.cos(4 * np.pi * x[1]) + 0.7


class BohachevskyFunction(Benchmark):
    def evaluate(self, x, y):
        return x ** 2 + 2 * y ** 2 - 0.3 * np.cos(3 * np.pi * x) - 0.4 * np.cos(4 * np.pi * y) + 0.7

    @property
    def dimensions(self):
        return 2

    def find_best_solution(self, solutions):
        return solutions[np.array([self.evaluate(*x) for x in solutions]).argmin()]


class EasomFunction(Benchmark):
    def evaluate(self, x, y):
        return -np.cos(x) * np.cos(y) * np.exp(-(x - np.pi) ** 2 - (y - np.pi) ** 2)

    @property
    def dimensions(self):
        return 2

    def find_best_solution(self, solutions):
        print(solutions)
        return solutions[np.array([self.evaluate(*x) for x in solutions]).argmin()]