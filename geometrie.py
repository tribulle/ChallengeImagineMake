"""
Cette classe permet de définir des fonctions pour la géométrie
"""
import math

class geometrie:
    @staticmethod
    def dist_eucl(x1,x2):
        return math.sqrt((x1.x-x2.x)**2+(x1.y-x2.y)**2+(x1.z-x2.z)**2)
    
    @staticmethod
    def produit_scalaire(v1,v2):
        return math.abs(v1.x*v2.x + v1.y*v2.y + v1.z*v2.z)
    

