import numpy as np


class SwarmIntelligence:
    def __init__(self, benchmark):
        self.solutions = []
        self.global_solution = None
        self.benchmark = benchmark

    def save_current_solutions(self, agents):
        self.solutions.append(np.array(agents))

