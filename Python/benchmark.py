import numpy as np


class Benchmark:
    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    def is_in_domain(self, *args, **kwargs):
        raise NotImplementedError()


class BohachevskyFunction(Benchmark):
    def evaluate(self, x, y):
        return np.power(x, 2) + 2 * np.power(y, 2) + (-0.3 * np.cos(3 * np.pi * x)) + (-0.4 * np.cos(4 * np.pi * y)) + 0.7

    def is_in_domain(self, x, y):
        return 0 < x < 10 and -5 < y < 5


class OutOfDomainException(Exception):
    pass


if __name__ == "__main__":
    print(BohachevskyFunction().evaluate(0, 0))
