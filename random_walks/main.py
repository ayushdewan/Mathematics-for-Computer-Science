# Math Libraries
import numpy as np

# Graphing libraries
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns

nx = ny = 51
data = np.zeros((nx, ny))

def animate_heat_map():
    fig = plt.figure()

   
    data[nx // 2, ny // 2] = 1
    ax = sns.heatmap(data, vmin=0, vmax=1, cmap="YlGnBu")

    def init():
        plt.clf()
        ax = sns.heatmap(data, vmin=0, vmax=1, cmap="YlGnBu")

    def animate(i):
        global data
        plt.clf()
        new_data = np.zeros((nx, ny))
        
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        bias = [0.125 for i in range(8)]

        assert sum(bias) == 1

        for i in range(nx):
            for j in range(ny):
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni >= 0 and ni < nx and nj >= 0 and nj < ny:
                        new_data[ni, nj] += bias[k] * data[i, j]
                    else:
                        new_data[i, j] += bias[k] * data[i, j]
        
        for i in range(nx):
            for j in range(ny):
                data[i, j] = new_data[i, j]

        ax = sns.heatmap(data, vmin=0, vmax=np.max(data), cmap="YlGnBu")

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=10)

    plt.show()

animate_heat_map()