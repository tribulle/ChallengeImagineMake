import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt
from plyfile import PlyData

# Chargez le fichier PLY
plydata = PlyData.read('Data/ear_back.ply')

# Accédez aux données des nuages de points
x = plydata['vertex']['x']
y = plydata['vertex']['y']
z = plydata['vertex']['z']

# Convertissez les données en tableaux NumPy
points = np.vstack((x, y, z)).T

# Create a pyvista point cloud object
cloud = pv.PolyData(points)

# Generate the mesh
mesh = cloud.delaunay_2d()

# Plot the mesh
plotter = pv.Plotter()
plotter.add_mesh(mesh, color='white')
plotter.show()

# Save the mesh to a file
mesh.save('mesh.vtk')

# Visualize the mesh with matplotlib
pv.plot(mesh)
plt.show()


