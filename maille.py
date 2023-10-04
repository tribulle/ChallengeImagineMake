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
    Calcul de l'aire du triangle
    """
    def calcul_surface(self):
        if(len(self.points)==3):
            d1 = geometrie.geometrie.dist_eucl(self.points[0],self.points[1])
            d2 = geometrie.geometrie.dist_eucl(self.points[1],self.points[2])
            d3 = geometrie.geometrie.dist_eucl(self.points[2],self.points[0])
            p = (d1 + d2 + d3)/2
            return math.sqrt(p*(p-d1)*(p-d2)*(p-d3))
        else:
            print("Erreur, la maille ne contient pas 3 elts")
    
    def afficher_points(self):
        print("=== NOUVELLE MAILLE ===")
        for i in self.points:
            i.afficher_point()





    