import numpy as np


class Benchmark:
    def evaluate(self, *args, **kwargs):
        pass


class MathFunction(Benchmark):
    def __init__(self):
        self.domain = None

    def evaluate(self, x, y):
        pass

    def is_in_domain(self, x, y):
        return self.domain(x, y)


class BohachevskyFunction(MathFunction):
    def evaluate(self, x, y):
        return np.power(x, 2) + 2 * np.power(y, 2) + (-0.3 * np.cos(3 * np.pi * x)) + (-0.4 * np.cos(4 * np.pi * y)) + 0.7


class Room(Benchmark):
    pass


if __name__ == "__main__":
    print(BohachevskyFunction().evaluate(0, 0))
