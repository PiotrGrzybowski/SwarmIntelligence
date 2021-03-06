class Benchmark:
    def evaluate(self, *args, **kwargs):
        raise NotImplementedError()

    @property
    def dimension(self):
        raise NotImplementedError()

    def find_best_solution(self, solutions):
        raise NotImplementedError()

    def evaluate_best_solution(self, solutions):
        return self.evaluate(*self.find_best_solution(solutions))

    def process_borders(self, *args, **kwargs):
        raise NotImplementedError()

    def is_maximising(self):
        raise NotImplementedError()

    def is_solution_better_than_global_solution(self, solution, global_solution):
        raise NotImplementedError()
