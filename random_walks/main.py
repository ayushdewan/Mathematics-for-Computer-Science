# Math Libraries
import numpy as np

# Graphing libraries
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns

# change grid size, preferably odd values
nx = ny = 21
data = np.zeros((nx, ny))

# change movement directions and probabilities
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
bias = [0.125 for i in range(8)]
assert sum(bias) == 1

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

        # compute next iteration
        peak = 0
        new_data = np.zeros((nx, ny))
        for i in range(nx):
            for j in range(ny):
                for k in range(len(dx)):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if ni >= 0 and ni < nx and nj >= 0 and nj < ny:
                        new_data[ni, nj] += bias[k] * data[i, j]
                        peak = max(peak, new_data[ni, nj])
                    else:
                        new_data[i, j] += bias[k] * data[i, j]
                        peak = max(peak, new_data[i, j])
                    
        
        # copy next iteration over
        data = np.copy(new_data)

        ax = sns.heatmap(data, vmin=0, vmax=peak, cmap="YlGnBu")

    anim = animation.FuncAnimation(fig, animate, init_func=init, interval=100)

    plt.show()

animate_heat_map()