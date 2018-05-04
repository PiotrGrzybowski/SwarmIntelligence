import yaml

from algorithms.bat_algorithm import BatAlgorithm
from algorithms.gray_wolf_algorithm import GrayWolfAlgorithm
from algorithms.particle_swarm_optimization import ParticleSwarmOptimization
from benchmarks.math_functions import easom_function, bohachevsky_function, BohachevskyFunction
from room import Room
from visualization.animations import animation
from shapely.geometry import box

# bat = BatAlgorithm(n=50, function=bohachevsky_function, low=-10, high=10, dimension=2, iterations=200)
# wolf = GrayWolfAlgorithm(n=50, function=easom_function, low=-10, high=10, dimension=2, iterations=200)


benchmark = BohachevskyFunction()
pso = ParticleSwarmOptimization(benchmark=benchmark, low=-10, high=10)

pso.find_best_solutions(number_of_agents=50, iterations=40, c1=1, c2=1)

print(len(pso.solutions))
# animation(pso.solutions, bohachevsky_function, -10, 10)

room = Room(400, 400)
room.load_from_yml('../room.yml')
pso.best_average_summary()
# with open('../room.yml') as f:
#     data = yaml.safe_load(f)
#     b = box(-5, -5, 5, 5)
#     a = -0.0
#     print(a)
#     print(b.centroid.x)
#     print(b)
#     # things = [Thing(**v) for v in data.values()]
#     #
#     # for thing in things:
#     #     room.add_thing(thing)