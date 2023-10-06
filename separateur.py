import point
import maille
import vecteur
import geometrie


#Coefficient qui gère à quel point on définit que qqch est du sol / plafond
coeff = 0.4


class separateur:
    """
    Permet de séparer les points
    """
    
    @staticmethod
    def devant_derriere(p : point):
        """
        Sépare les points selon si on est devant ou derière le plan YZ
        """
        if(p.y >= 0):
            return True
        return False
    
    
    @staticmethod
    def mur_sol_plafond(m : maille):
        """
        Sépare les mailles selon le sol (Z+- = 0) et les murs
        """
        z = vecteur.vecteur(0,1,0)
        v = geometrie.geometrie.vecteur_normal(m)
        x = geometrie.geometrie.produit_scalaire(z,v)
        midd= m.centre()
        if(x>coeff): #Dans ce cas on a du sol ou plafond
            if(midd.y>0): #cas plafond
                m.set_type(2)
                return
            else:
                m.set_type(1)
                return
        else:
            m.set_type(0)
            return

