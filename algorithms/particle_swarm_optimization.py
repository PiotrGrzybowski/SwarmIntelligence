import numpy as np

from algorithms.swarm_intelligence import SwarmIntelligence


class ParticleSwarmOptimization(SwarmIntelligence):
    def __init__(self, benchmark, low, high):
        super().__init__(benchmark)
        self.low = low
        self.high = high

        self.agents = None
        self.velocity = None

    def find_best_solution(self, iterations, number_of_agents, c1, c2):
        self.initialize_searching(number_of_agents)

        best_solution = self.agents[np.array([self.benchmark.evaluate(*x) for x in self.agents]).argmin()]
        self.global_solution = best_solution
        for i in range(iterations):
            r1 = np.random.random((number_of_agents, self.benchmark.dimension))
            r2 = np.random.random((number_of_agents, self.benchmark.dimension))

            self.process_agents(best_solution, c1, c2, r1, r2)
            self.save_current_solutions(self.agents)
            best_solution = self.benchmark.find_best_solution(self.agents)
            self.update_global_solution(best_solution)

    def process_agents(self, best_solution, c1, c2, r1, r2):
        self.update_velocity(best_solution, c1, c2, r1, r2)
        self.agents += self.velocity
        self.agents = np.clip(self.agents, self.low, self.high)

    def initialize_searching(self, number_of_agents):
        self.solutions = []
        self.agents = np.random.uniform(self.low, self.high, (number_of_agents, self.benchmark.dimension))
        self.velocity = np.zeros((number_of_agents, self.benchmark.dimension))
        self.save_current_solutions(self.agents)

    def update_velocity(self, best_solution, c1, c2, r1, r2):
        self.velocity = 0.5 * self.velocity + c1 * r1 * (best_solution - self.agents) + c2 * r2 * (self.global_solution - self.agents)

    def update_global_solution(self, best_solution):
        if self.benchmark.evaluate(*best_solution) < self.benchmark.evaluate(*self.global_solution):
            self.global_solution = best_solution

    def initialize_agents(self, number_of_agents):
        self.agents = np.random.uniform(self.low, self.high, (number_of_agents, self.benchmark.dimension))

    def initialize_velocity(self, number_of_agents):
        self.velocity = np.zeros((number_of_agents, self.benchmark.dimension))