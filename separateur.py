import point
import maille
import vecteur
import geometrie


#Coefficient qui gère à quel point on définit que qqch est du sol / plafond
coeff = 0.8
"""
Permet de séparer les points
"""

class separateur:

    """
    Sépare les points selon si on est devant ou derière le plan YZ
    """
    @staticmethod
    def devant_derriere(p):
        if(p.y >= 0):
            return True
        return False
    
    """
    Sépare les mailles selon le sol (Z+- = 0) et les murs
    """
    @staticmethod
    def mur_sol_plafond(m):
        z = vecteur.vecteur(0,0,1)
        v = geometrie.geometrie.vecteur_normal(m)
        x = geometrie.geometrie.produit_scalaire(z,v)
        if(x>coeff): #Dans ce cas on a du sol ou plafond
            if(m.liste_points[0].z>0): #cas plafond
                m.set_type(2)
                return
            else:
                m.set_type(1)
                return
        else:
            m.set_type(0)
            return

