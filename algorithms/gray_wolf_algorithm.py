import numpy as np

from algorithms.swarm_intelligence import SwarmIntelligence


class GrayWolfAlgorithm(SwarmIntelligence):
    def __init__(self, benchmark, low, high):
        super().__init__(benchmark)
        self.low = low
        self.high = high
        self.alpha = []
        self.beta = []
        self.delta = []
        self.agents = []

    def initialize_searching(self, number_of_agents):
        self.solutions = []
        self.agents = np.random.uniform(self.low, self.high, (number_of_agents, self.benchmark.dimension))
        self.save_current_solutions(self.agents)
        self.evaluate_alpha_beta_delta(number_of_agents)
        self.global_solution = self.alpha

    def find_best_solution(self, iterations, number_of_agents):
        self.initialize_searching(number_of_agents)

        for t in range(iterations):
            a = 2 - 2 * t / iterations

            r1 = np.random.random((number_of_agents, self.benchmark.dimension))
            r2 = np.random.random((number_of_agents, self.benchmark.dimension))
            A1 = 2 * r1 * a - a
            C1 = 2 * r2

            r1 = np.random.random((number_of_agents, self.benchmark.dimension))
            r2 = np.random.random((number_of_agents, self.benchmark.dimension))
            A2 = 2 * r1 * a - a
            C2 = 2 * r2

            r1 = np.random.random((number_of_agents, self.benchmark.dimension))
            r2 = np.random.random((number_of_agents, self.benchmark.dimension))
            A3 = 2 * r1 * a - a
            C3 = 2 * r2

            Dalpha = abs(C1 * self.alpha - self.agents)
            Dbeta = abs(C2 * self.beta - self.agents)
            Ddelta = abs(C3 * self.delta - self.agents)

            X1 = self.alpha - A1 * Dalpha
            X2 = self.beta - A2 * Dbeta
            X3 = self.delta - A3 * Ddelta

            self.agents = (X1 + X2 + X3) / 3

            # self.agents = self.benchmark.process_borders(self.agents, self.low, self.high)
            self.save_current_solutions(self.agents)

            self.evaluate_alpha_beta_delta(number_of_agents)
            if self.benchmark.is_solution_better_than_global_solution(self.alpha, self.global_solution):
                self.global_solution = self.alpha
        self.evaluate_alpha_beta_delta(number_of_agents)

    def evaluate_alpha_beta_delta(self, n):
        fitness = sorted([(self.benchmark.evaluate(*self.agents[i]), i) for i in range(n)], reverse=self.benchmark.is_maximising())
        self.alpha = self.agents[fitness[0][1]]
        self.beta = self.agents[fitness[1][1]]
        self.delta = self.agents[fitness[2][1]]
