import structure
import numpy as np
import pyvista as pv
import sys

def list_to_str(list):
    str_v = ''
    for i in list:
        str_v += ";"+str(i)
    return str_v


def restructuration(liste_points,face_sequence):
    """
    Permet de renvoyer les points utiles
    """
    liste_points_f = []
    liste_indices = [0 for i in range(len(liste_points))]
    i = 0
    while i < len(face_sequence):
        nb_elt = face_sequence[i]
        for k in range(nb_elt):
            if(liste_indices[face_sequence[i+k+1]]==0):
                liste_indices[face_sequence[i+k+1]]=1
                liste_points_f.append(liste_points[face_sequence[i+k+1]])
        i += nb_elt+1
    return liste_points_f
        

def classification(structure, points):
    
    # Les listes des faces (format PyVista)
    liste_face_0 = np.array([])
    liste_face_1 = np.array([])
    liste_face_2 = np.array([])
    points_0 = []
    points_1 = []
    points_2 = []

    for m in structure.liste_mailles:
        for i in range(len(m.points)):
            if m.type == 0:
                points_0.append(m.points[i].retour_liste())
            elif m.type == 1:
                points_1.append(m.points[i].retour_liste())
            else:
                points_2.append(m.points[i].retour_liste())

    
    return (np.array(points_0), np.array(points_1), np.array(points_2))








