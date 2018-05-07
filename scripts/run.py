import numpy as np

import yaml
import matplotlib.pyplot as plt
from matplotlib.pylab import savefig

from Python.room import Room
from Python.thing import Thing
from Python.visualization_utils import RoomDrawer
from algorithms.gray_wolf_algorithm import GrayWolfAlgorithm
from algorithms.particle_swarm_optimization import ParticleSwarmOptimization
from algorithms.whale_swarm_optimization import WhaleSwarmAlgorithm
from benchmarks.math_functions import BohachevskyFunction, Ackley2Function, HolderTableFunction
from visualization.animations import animation, animation3D
from shapely.geometry import box

# # benchmark = BohachevskyFunction()
# benchmark = Ackley2Function()
# # benchmark = BohachevskyFunction()
# # benchmark = HolderTableFunction()
# low = -10
# high = 10
# iterations = 40
# number_of_agents = 30
#
# k = 1
# whale = WhaleSwarmAlgorithm(benchmark=benchmark, low=low, high=high)
# pso = ParticleSwarmOptimization(benchmark=benchmark, low=low, high=high)
# wolf = GrayWolfAlgorithm(benchmark=benchmark, low=low, high=high)
#
# res = np.zeros(3)
#
# pso.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1, c1=0.5, c2=0.5)
# wolf.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1)
# whale.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1, ro0=3, eta=0.001)
#
# pso_best, _ = pso.best_average_summary()
# wolf_best, _ = wolf.best_average_summary()
# whale_best, _ = whale.best_average_summary()
# delta = -19
#
# while pso_best[-1] > delta or wolf_best[-1] > delta or whale_best[-1] > delta:
#     pso.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1, c1=0.3, c2=0.7)
#     wolf.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1)
#     whale.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1, ro0=2, eta=0.01)
#
#     pso_best, _ = pso.best_average_summary()
#     wolf_best, _ = wolf.best_average_summary()
#     whale_best, _ = whale.best_average_summary()
#     if pso_best[-1] < delta:
#         res[0] += 1
#     if wolf_best[-1] < delta:
#         res[1] += 1
#     if whale_best[-1] < delta:
#         res[2] += 1
#     k += 1
#     print(k)
#
# print(res / k)
# print(pso_best[-1])
# print(wolf_best[-1])
# print(whale_best[-1])
#
# plt.plot(np.arange(iterations), pso_best, label='pso best')
# plt.plot(np.arange(iterations), wolf_best, label='wolf best')
# plt.plot(np.arange(iterations), whale_best, label='whale best')
# # plt.plot(np.arange(iterations), average, label='average')
# plt.xlabel('iterations')
# plt.ylabel('evaluation')
# plt.title('Best evaluation on each iteration for Holder Table Function.')
# plt.legend()
# savefig('patest.jpg')
# animation(pso.solutions, benchmark, low, high)
# animation(wolf.solutions, benchmark, low, high)
# animation(whale.solutions, benchmark, low, high)
# animation3D(wolf.solutions, benchmark, low, high)

room = Room(400, 400)
room.load_from_yml('../room.yml')

benchmark = room
number_of_agents = 40
iterations = 20
low = -200
high = 200

wolf = GrayWolfAlgorithm(benchmark=benchmark, low=low, high=high)
wolf.find_best_solution(number_of_agents=number_of_agents, iterations=iterations - 1)

wolf = GrayWolfAlgorithm(benchmark=benchmark, low=low, high=high)
print(wolf.global_solution)
drawer = RoomDrawer(room)
drawer.show()