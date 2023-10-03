import geometrie
import point
import math

"""
Cette classe permet de définir des mailles (sets de 3 points)
pour créer une géométrie de base
"""

class maille:
    def __init__(self,face,liste_points):
        self.points = []
        for i in range(len(face)):
            p = point.point()
            p.set_xyz(liste_points[face[i]])
            self.points.append(p)
    """
    Calcul d'un triangle
    """
    def calcul_surface(self):
        d1 = geometrie.geometrie.dist_eucl(self.points[0],self.points[1])
        d2 = geometrie.geometrie.dist_eucl(self.points[1],self.points[2])
        return (d1**2 - (d2/2)**2)*d2/2




    