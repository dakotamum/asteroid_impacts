import pyvista as pv
import numpy as np
import os

from matplotlib.colors import ListedColormap, BoundaryNorm

def make_snapshot(filename):
    filename = filename

    print("Reading volume dataset from " + filename + " ...")
    data = pv.read(filename)  
    print("Done!")

    water = np.array(data['v02'])

    water_3d = water.reshape(300, 300, 300)
    water_3d = np.transpose(water_3d, axes=(2, 0, 1))

    grid = pv.UniformGrid()
    grid.dimensions = water_3d.shape
    grid.origin = (0, 0, 0)
    grid.spacing = (1, 1, 1)
    grid.point_data["Data"] = water_3d.flatten(order="F")

    plotter = pv.Plotter(off_screen=True)
    plotter.cammera_position = "yz"
    plotter.enable_parallel_projection()
    slice = grid.slice(normal=[1, 1, 0])

    plotter.add_mesh(slice)
    png_filename = filename + ".png"
    plotter.show(screenshot=png_filename)

directory = 'a31'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    make_snapshot(f)