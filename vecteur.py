"""
Classe qui défini des vecteurs
"""
import point 
class vecteur : 
    def __init__ (self, x, y ,z):
        self.x = x
        self.y = y
        self.z = z 

    @staticmethod
    def vect_directeur(a : point, b : point):

        # Calcul des composantes du vecteur directeur
        dx = b.x- a.x
        dy = b.y - a.y
        dz = b.z - a.z

        return vecteur(dx, dy, dz)