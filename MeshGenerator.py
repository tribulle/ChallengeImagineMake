import numpy as np
import pyvista as pv
import matplotlib.pyplot as plt
from plyfile import PlyData
import structure
import classification

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
    print("Le volume total est : "+str(mesh.volume))

    # Create new mesh (wall, floor, ceilling)
    liste_mesh = classification.classification(s,points)
    mesh_0 = liste_mesh[0]
    mesh_1 = liste_mesh[1]
    mesh_2 = liste_mesh[2]

    s_0 = structure.structure()
    surf_0 = mesh_0.extract_surface()
    s_0.init_mailles(surf_0.faces,surf_0.points)

    s_1 = structure.structure()
    surf_1 = mesh_1.extract_surface()
    s_1.init_mailles(surf_1.faces,surf_1.points)

    s_2 = structure.structure()
    surf_2 = mesh_2.extract_surface()
    s_2.init_mailles(surf_2.faces,surf_2.points)

    print("La surface totale des murs est : "+str(s_0.calcul_surface_tot()))
    print("La surface totale du sol est : "+str(s_1.calcul_surface_tot()))
    print("La surface totale du plafond est : "+str(s_2.calcul_surface_tot()))

    # Plot the mesh
    plotter = pv.Plotter()
    plotter.add_mesh(mesh_0, color='grey')
    plotter.add_mesh(mesh_1, color='red')
    plotter.add_mesh(mesh_2, color='blue')
    plotter.show()

    # Save the mesh to a file
    #mesh.save('mesh.vtk')

    # Visualize the mesh with matplotlib
