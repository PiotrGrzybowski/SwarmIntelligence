class SwarmIntelligence:
    def __init__(self):
        self.solutions = []
        self.global_solution = None

    def save_current_solutions(self, agents):
        self.solutions.append([list(i) for i in agents])
