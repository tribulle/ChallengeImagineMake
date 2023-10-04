import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt
from plyfile import PlyData
import structure

# Chargez le fichier PLY
plydata = PlyData.read('Data/ear_back.ply')

# Acc�dez aux donn�es des nuages de points
x = plydata['vertex']['x']
y = plydata['vertex']['y']
z = plydata['vertex']['z']

# Convertissez les donn�es en tableaux NumPy
points = np.vstack((x, y, z)).T

def MeshGenerator(points):
    # Create a pyvista point cloud object
    cloud = pv.PolyData(points)

    # Generate the mesh
    mesh = cloud.delaunay_3d() #cloud.reconstruct_surface(nbr_sz=20) #
    s = structure.structure()
    surf = mesh.extract_surface()
    s.init_mailles(surf.faces,surf.points)
    print("La surface totale est : "+str(s.calcul_surface_tot()))
    # Plot the mesh
    plotter = pv.Plotter()
    plotter.add_mesh(mesh, color='white')
    plotter.show()

    # Save the mesh to a file
    #mesh.save('mesh.vtk')

    # Visualize the mesh with matplotlib
