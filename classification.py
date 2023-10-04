import structure
import numpy as np

def classification(structure, mesh_0, mesh_1, mesh_2):
    
    # Les listes des faces (format PyVista)
    liste_face_0 = []
    liste_face_1 = []
    liste_face_2 = []

    for m in structure.liste_mailles:
        taille = len(m.face)
        face_sequence = np.hstack([taille],m.face)

        if m.type == 0:
            liste_face_0.append(face_sequence)
        elif m.type == 1:
            liste_face_1.append(face_sequence)
        else:
            liste_face_2.append(face_sequence)

    # Les listes en format numpy
    array_0 = np.array(liste_face_0)
    array_1 = np.array(liste_face_1)
    array_2 = np.array(liste_face_2)

    mesh_0







