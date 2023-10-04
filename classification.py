import structure
import numpy as np
import pyvista as pv

def classification(structure, points):
    
    # Les listes des faces (format PyVista)
    liste_face_0 = np.array([])
    liste_face_1 = np.array([])
    liste_face_2 = np.array([])
    mesh_0 = None
    mesh_1 = None
    mesh_2 = None

    for m in structure.liste_mailles:
        taille = len(m.face)
        face_sequence = np.hstack(([taille],m.face)).astype('i')
        if m.type == 0:
            liste_face_0 = np.hstack((liste_face_0,face_sequence)).astype('i')
        elif m.type == 1:
            liste_face_1 = np.hstack((liste_face_1,face_sequence)).astype('i')
        else:
            liste_face_2 = np.hstack((liste_face_2,face_sequence)).astype('i')

    if(len(liste_face_0)>0):
        mesh_0 = pv.PolyData(points, liste_face_0)
        print(mesh_0)
    if(len(liste_face_1)>0):
        mesh_1 = pv.PolyData(points, liste_face_1)
    if(len(liste_face_2)>0):
        mesh_2 = pv.PolyData(points, liste_face_2)

    liste_return = [mesh_0, mesh_1, mesh_2]
    return liste_return








