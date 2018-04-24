from algorithms.bat_algorithm import BatAlgorithm
from algorithms.gray_wolf_algorithm import GrayWolfAlgorithm
from algorithms.particle_swarm_intelligence import ParticleSwarmIntelligence
from benchmarks.math_functions import easom_function, bohachevsky_function
from visualization.animations import animation

alh = ParticleSwarmIntelligence(n=50, function=bohachevsky_function, low=-10, high=10, dimension=2, iterations=40, c1=1, c2=1)
bat = BatAlgorithm(n=50, function=bohachevsky_function, low=-10, high=10, dimension=2, iterations=200)
wolf = GrayWolfAlgorithm(n=50, function=easom_function, low=-10, high=10, dimension=2, iterations=200)

animation(wolf.solutions, easom_function, -10, 10)

