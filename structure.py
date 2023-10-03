"""
Permet de définir une collection de mailles
"""
import maille

class structure:
    def __init__(self):
        self.liste_mailles = []

    """
    Initialise la liste de mailles à partir du mesh
    """
    def init_mailles(self,liste_faces,liste_points):
        i = 0
        while i < len(liste_faces):
            liste = []
            for j in range(i,i+liste_faces[i]+1,1):
                liste.append(liste_faces[j])
            self.liste_mailles.append(maille.maille(liste,liste_points))
            i += liste_faces[i]+1
    
    def calcul_surface_tot(self):
        total = 0
        for i in self.liste_mailles:
            total += i.calcul_surface()
        return total