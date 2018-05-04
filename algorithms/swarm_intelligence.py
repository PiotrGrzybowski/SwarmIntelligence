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
            print(self.solutions[i])