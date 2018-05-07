import numpy as np


class SwarmIntelligence:
    def __init__(self, benchmark):
        self.solutions = []
        self.global_solution = None
        self.benchmark = benchmark

    def save_current_solutions(self, agents):
        self.solutions.append([list(i) for i in agents])

    def best_average_summary(self):
        best_results = []
        average_results = []

        for i in range(len(self.solutions)):
            best_results.append(self.benchmark.evaluate_best_solution(self.solutions[i]))
            average_results.append(np.mean([self.benchmark.evaluate(*solution) for solution in self.solutions[i]]))
        return best_results, average_results
