
import maille
import separateur

class structure:
    """
    Permet de définir une collection de mailles
    """
    def __init__(self):
        self.liste_mailles = []

    
    def init_mailles(self,liste_faces : list,liste_points : list):
        """
        Initialise la liste de mailles à partir du mesh
        """
        i = 0
        while i < len(liste_faces):
            liste = []
            for j in range(i+1,i+liste_faces[i]+1,1):
                liste.append(liste_faces[j])
            self.liste_mailles.append(maille.maille(liste,liste_points))
            i += liste_faces[i]+1
    
    def calcul_surface_tot(self):
        total = [0,0,0]
        for i in self.liste_mailles:
            total[i.type] += i.calcul_surface()
        return total
    
    def afficher_mailles(self):
        for i in self.liste_mailles:
            i.afficher_points()


    def set_types(self):
        """
        Définit le type (sol/mur/plafond) de toutes les mailles de la structure
        """
        for i in self.liste_mailles:
            separateur.separateur.mur_sol_plafond(i)