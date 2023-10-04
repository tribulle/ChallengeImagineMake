"""
Cette classe permet de définir des fonctions pour la géométrie
"""
import math
import vecteur
import maille
import point

class geometrie:
    @staticmethod
    def dist_eucl(x1 : point,x2 : point):
        """
        Calcule la distance euclidienne entre deux points
        """
        return math.sqrt((x1.x-x2.x)**2+(x1.y-x2.y)**2+(x1.z-x2.z)**2)
    
    
    @staticmethod
    def produit_scalaire(v1 : vecteur,v2 : vecteur):
        """
        Définit le produit scalaire entre de vecteurs de la classe vecteur
        """
        return abs(v1.x*v2.x + v1.y*v2.y + v1.z*v2.z)
    
    @staticmethod
    def normaliser(v : vecteur):
        """
        Renvoie un vecteur normalisé du vecteur passé en paramètre
        """
        norme = math.sqrt(geometrie.produit_scalaire(v,v))
        if(norme == 0):
            print("Problème, vecteur nul !")
            return vecteur.vecteur(0,0,0)
        return vecteur.vecteur(v.x/norme,v.y/norme,v.z/norme)
    
    
    @staticmethod
    def produit_vectoriel(v1,v2):
        """
        Retourne le produit scalaire de deux vecteurs
        """
        x = v1.y*v2.z-v1.z*v2.y
        y = v1.z*v2.x-v1.x*v2.z
        z = v1.x*v2.y - v1.y*v2.x
        return vecteur.vecteur(x,y,z)


    @staticmethod
    def vecteur_normal(m):
        """
        Retourne le vecteur normal normalisé d'une maille
        """
        if(len(m.points)!=3):
            print("Erreur, la face ne contient pas 3 points !")
            return vecteur(0,0,0)
        x = m.points[0]
        y = m.points[1]
        z = m.points[2]
        v1 = vecteur.vecteur(0,0,0)
        v2 = vecteur.vecteur(0,0,0)
        v1.vect_directeur(x,y)
        v2.vect_directeur(y,z)
        return geometrie.normaliser(geometrie.produit_vectoriel(v1,v2))
        
    

