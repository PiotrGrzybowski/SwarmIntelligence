import numpy as np
from random import random

from algorithms.swarm_intelligence import SwarmIntelligence


class BatAlgorithm(SwarmIntelligence):
    def __init__(self, n, benchmark, low, high, dimension, iterations, r0=0.9, V0=0.5, fmin=0, fmax=0.02, alpha=0.9,
                 csi=0.9):

        super().__init__(benchmark)
        r = [r0 for i in range(n)]

        self.agents = np.random.uniform(low, high, (n, dimension))
        self.save_current_solutions(self.agents)

        velocity = np.zeros((n, dimension))
        V = [V0] * n

        best_solution = self.agents[np.array([benchmark(i) for i in self.agents]).argmin()]
        self.global_solution = best_solution

        f = fmin + (fmin - fmax)

        for t in range(iterations):

            sol = self.agents

            F = f * np.random.random((n, dimension))
            velocity += (self.agents - self.global_solution) * F
            sol += velocity

            for i in range(n):
                if random() > r[i]:
                    sol[i] = self.global_solution + np.random.uniform(-1, 1, (1, dimension)) * sum(V) / n

            for i in range(n):
                if benchmark(sol[i]) < benchmark(self.agents[i]) and random() < V[i]:
                    self.agents[i] = sol[i]
                    V[i] *= alpha
                    r[i] *= (1 - np.exp(-csi * t))

            self.agents = np.clip(self.agents, low, high)
            self.save_current_solutions(self.agents)

            best_solution = self.agents[np.array([benchmark(x) for x in self.agents]).argmin()]
            if benchmark(best_solution) < benchmark(self.global_solution):
                self.global_solution = best_solution
