import matplotlib.pyplot as plt
import numpy as np
from plotly.tools import mpl_to_plotly
import chart_studio.plotly as py




def interactive_grid(n):
    n = 25
    #Create a grid of a certain size, zeros as place holders
    dummy_grid = np.zeros((n,n))

    fig = plt.figure(figsize=(n,n))

    ax = plt.axes()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    #plotting this grid, it's boring for now, all white, since the grid is nothing but zeros
    im = ax.imshow(dummy_grid,cmap='binary')
    #Plotting lines to demarcate the cells in the grid
    for n in range(0,len(dummy_grid)):
        plt.axvline(.5+n)
        plt.axhline(.5+n)
    # to track selected/deselected points
    startup_points = []
        #keeping input live indefinitely
    plt.ion()
    while plt.isinteractive():
        try:
            #ginput, looking for 1 value at a time, setting timeout to -1 means it will wait indefinetely
            pt = plt.ginput(1, timeout=-1)
            #getting coordinates, rounded to whole numbers
            p_1 = int(round(pt[0][1],0))
            p_2 = int(round(pt[0][0],0))
            coord = (p_2,len(dummy_grid)-p_1-1)
            #updating the tracking of which points have been selected, and changing the display grid
            if coord in startup_points:
                dummy_grid[p_1][p_2] = 0
                startup_points.remove(coord)
            else:
                dummy_grid[p_1][p_2] = 1
                startup_points.append(coord)
            #update the displayed grid
            plt.imshow(dummy_grid,cmap='binary')
        except IndexError:
            url = py.plot_mpl(fig, filename='interactive_grid')
            print(url)
            return startup_points