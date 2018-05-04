from matplotlib import pyplot as plt
import matplotlib.animation
import numpy as np


def animation(agents, function, lb, ub):
    side = np.linspace(lb, ub, (ub - lb) * 5)
    X, Y = np.meshgrid(side, side)
    Z = np.array([np.array([function([X[i][j], Y[i][j]]) for j in range(len(X))]) for i in range(len(X[0]))])

    fig = plt.figure()
    plt.axes(xlim=(lb, ub), ylim=(lb, ub))
    plt.pcolormesh(X, Y, Z, shading='gouraud', cmap='RdBu_r')
    plt.colorbar()

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    def an(i):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(agents) - 1)
    plt.show()