"""
Cette classe permet de définir des fonctions pour la géométrie
"""
import math
import vecteur
import maille

class geometrie:
    @staticmethod
    def dist_eucl(x1,x2):
        return math.sqrt((x1.x-x2.x)**2+(x1.y-x2.y)**2+(x1.z-x2.z)**2)
    
    """
    Définit le produit scalaire entre de vecteurs de la classe vecteur
    """
    @staticmethod
    def produit_scalaire(v1,v2):
        return math.abs(v1.x*v2.x + v1.y*v2.y + v1.z*v2.z)
    
    @staticmethod
    def normaliser(v):
        norme = math.sqrt(geometrie.produit_scalaire(v,v))
        return vecteur.vecteur(v.x/norme,v.y/norme,v.z/norme)
    
    """
    Retourne le produit scalaire de deux vecteurs
    """
    @staticmethod
    def produit_vectoriel(v1,v2):
        x = v1.y*v2.z-v1.z*v2.y
        y = v1.z*v2.x-v1.x*v2.z
        z = v1.x*v2.y - v1.y*v2.x
        return vecteur(x,y,z)

    """
    Retourne le vecteur normal normalisé d'une maille
    """
    @staticmethod
    def vecteur_normal(m):
        if(len(m.liste_points)!=3):
            print("Erreur, la face ne contient pas 3 points !")
            return vecteur(0,0,0)
        x = m.liste_points[0]
        y = m.liste_points[1]
        z = m.liste_points[2]
        v1 = vecteur.vecteur(0,0,0)
        v2 = vecteur.vecteur(0,0,0)
        v1.vect_directeur(x,y)
        v2.vect_directeur(y,z)
        return geometrie.normaliser(geometrie.produit_vectoriel(v1,v2))
        

