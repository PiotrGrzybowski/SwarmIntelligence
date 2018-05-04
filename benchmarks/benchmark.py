class Benchmark:
    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def dimensions(self):
        raise NotImplementedError()

    def find_best_solution(self, solutions):
        raise NotImplementedError()