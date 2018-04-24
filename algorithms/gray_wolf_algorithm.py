import numpy as np

from algorithms.swarm_intelligence import SwarmIntelligence


class GrayWolfAlgorithm(SwarmIntelligence):
    def __init__(self, n, function, low, high, dimension, iterations):
        super().__init__()
        self.agents = np.random.uniform(low, high, (n, dimension))
        self.save_current_solutions(self.agents)
        alpha, beta, delta = self.get_alpha_beta_delta(n, function)

        self.global_best = alpha

        for t in range(iterations):

            a = 2 - 2 * t / iterations

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A1 = 2 * r1 * a - a
            C1 = 2 * r2

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A2 = 2 * r1 * a - a
            C2 = 2 * r2

            r1 = np.random.random((n, dimension))
            r2 = np.random.random((n, dimension))
            A3 = 2 * r1 * a - a
            C3 = 2 * r2

            Dalpha = abs(C1 * alpha - self.agents)
            Dbeta = abs(C2 * beta - self.agents)
            Ddelta = abs(C3 * delta - self.agents)

            X1 = alpha - A1 * Dalpha
            X2 = beta - A2 * Dbeta
            X3 = delta - A3 * Ddelta

            self.agents = (X1 + X2 + X3) / 3

            self.agents = np.clip(self.agents, low, high)
            self.save_current_solutions(self.agents)

            alpha, beta, delta = self.get_alpha_beta_delta(n, function)
            if function(alpha) < function(self.global_best):
                self.global_best = alpha

        alpha, beta, delta = self.get_alpha_beta_delta(n, function)
        self.leaders = list(alpha), list(beta), list(delta)

    def get_alpha_beta_delta(self, n, function):

        result = []
        fitness = [(function(self.agents[i]), i) for i in range(n)]
        fitness.sort()

        for i in range(3):
            result.append(self.agents[fitness[i][1]])

        return result

    def get_leaders(self):
        """Return alpha, beta, delta leaders of grey wolfs"""

        return list(self.leaders)
