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

def une_fonction_qui_fait_des_trucs(plotter,mesh : pv.PolyData,type:int):
    if(mesh == None):
        return
    s = structure.structure()
    surf = mesh.extract_surface()
    s.init_mailles(surf.faces,surf.points)
    if(type==0):
        plotter.add_mesh(mesh, color='grey')
    if(type==1):
        plotter.add_mesh(mesh, color='red')
    if(type==2):
        plotter.add_mesh(mesh, color='blue')

def MeshGenerator(points):
    # Create a pyvista point cloud object
    cloud = pv.PolyData(points)

    # Generate the mesh
    mesh = cloud.delaunay_3d() #cloud.reconstruct_surface(nbr_sz=20) #
    s = structure.structure()
    surf = mesh.extract_surface()
    s.init_mailles(surf.faces,surf.points)
    s.set_types()
    print("La surface totale est : "+str(sum(s.calcul_surface_tot())))
    print("La surface des murs est : "+str(s.calcul_surface_tot()[0]))
    print("La surface du sol est : "+str(s.calcul_surface_tot()[1]))
    print("La surface du plafond est : "+str(s.calcul_surface_tot()[2]))
    print("Le volume total est : "+str(mesh.volume))

    # Create new mesh (wall, floor, ceilling)
    liste_mesh = classification.classification(s,points)
    mesh_0 = liste_mesh[0]
    mesh_1 = liste_mesh[1]
    mesh_2 = liste_mesh[2]

    # Plot the mesh
    plotter = pv.Plotter()
    une_fonction_qui_fait_des_trucs(plotter,mesh_0,0)
    une_fonction_qui_fait_des_trucs(plotter,mesh_1,1)
    une_fonction_qui_fait_des_trucs(plotter,mesh_2,2)
    plotter.show()

    # Save the mesh to a file
    #mesh.save('mesh.vtk')

    # Visualize the mesh with matplotlib
