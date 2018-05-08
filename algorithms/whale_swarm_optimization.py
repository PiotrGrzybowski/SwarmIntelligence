import numpy as np

from algorithms.swarm_intelligence import SwarmIntelligence


class WhaleSwarmAlgorithm(SwarmIntelligence):
    """
    Whale Swarm Algorithm
    """

    def __init__(self, benchmark, low, high):
        """
        :param number_of_agents: number of agents
        :param benchmark: test function
        :param low: lower limits for plot axes
        :param high: upper limits for plot axes
        :param iterations: the number of iterations
        :param ro0: intensity of ultrasound at the origin of source
        :param eta: probability of message distortion at large distances
        """

        super().__init__(benchmark)
        self.low = low
        self.high = high
        self.agents = []

    def find_best_solution(self, iterations, number_of_agents, ro0=2, eta=0.005):
        self.initialize_searching(number_of_agents)

        for t in range(iterations):
            new_agents = self.agents
            for i in range(number_of_agents):
                y = self.__better_and_nearest_whale(i, number_of_agents)
                if y:
                    new_agents[i] += np.dot(np.random.uniform(0, ro0 * np.exp(-eta * self.__whale_dist(i, y))),
                                            self.agents[y] - self.agents[i])
            self.agents = new_agents
            # self.agents = self.benchmark.process_borders(self.agents, self.low, self.high)
            self.save_current_solutions(self.agents)

            solution = self.benchmark.find_best_solution(self.agents)
            if self.benchmark.is_solution_better_than_global_solution(solution, self.global_solution):
                self.global_solution = solution

    def initialize_searching(self, number_of_agents):
        self.solutions = []
        self.agents = np.random.uniform(self.low, self.high, (number_of_agents, self.benchmark.dimension))
        self.save_current_solutions(self.agents)
        self.global_solution = self.benchmark.find_best_solution(self.agents)

    def __whale_dist(self, i, j):
        return np.linalg.norm(self.agents[i] - self.agents[j])

    def __better_and_nearest_whale(self, u, n):
        temp = float("inf")

        v = None
        for i in range(n):
            if self.benchmark.is_solution_better_than_global_solution(self.agents[i], self.agents[u]):
                dist_iu = self.__whale_dist(i, u)
                if dist_iu < temp:
                    v = i
                    temp = dist_iu
        return v
