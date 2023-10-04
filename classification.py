import structure
import numpy as np
import pyvista as pv

def classification(structure, mesh_base):
    
    # Les listes des faces (format PyVista)
    liste_face_0 = np.array([])
    liste_face_1 = np.array([])
    liste_face_2 = np.array([])

    for m in structure.liste_mailles:
        taille = len(m.face)
        face_sequence = np.hstack([taille],m.face)

        if m.type == 0:
            liste_face_0 = np.hstack(liste_face_0,face_sequence)
        elif m.type == 1:
            liste_face_1 = np.hstack(liste_face_1,face_sequence)
        else:
            liste_face_2 = np.hstack(liste_face_2,face_sequence)

        mesh_0 = pv.PolyData(mesh_base.extract_surface().points, liste_face_0)
        mesh_1 = pv.PolyData(mesh_base.extract_surface().points, liste_face_1)
        mesh_2 = pv.PolyData(mesh_base.extract_surface().points, liste_face_2)

        liste_return = [mesh_0, mesh_1, mesh_2]
        return liste_return








