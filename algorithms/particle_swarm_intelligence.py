import numpy as np

from algorithms.swarm_intelligence import SwarmIntelligence


class ParticleSwarmIntelligence(SwarmIntelligence):
    def __init__(self, n, function, low, high, dimension, iterations, c1=1, c2=1):
        super().__init__()
        self.agents = np.random.uniform(low, high, (n, dimension))
        velocity = np.zeros((n, dimension))
        self.save_current_solutions(self.agents)

        best_solution = self.agents[np.array([function(x) for x in self.agents]).argmin()]
        self.global_solution = best_solution

        for i in range(iterations):
            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))

            velocity = 0.5 * velocity + c1 * r1 * (best_solution - self.agents) + c2 * r2 * (self.global_solution - self.agents)

            self.agents += velocity
            self.agents = np.clip(self.agents, low, high)
            self.save_current_solutions(self.agents)

            best_solution = self.agents[np.array([function(x) for x in self.agents]).argmin()]

            if function(best_solution) < function(self.global_solution):
                self.global_solution = best_solution

