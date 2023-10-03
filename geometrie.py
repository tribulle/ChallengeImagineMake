"""
Cette classe permet de définir des fonctions pour la géométrie
"""
import math

class geometrie:
    @staticmethod
    def dist_eucl(x1,x2):
        return math.sqrt((x1.x-x2.x)**2+(x1.y-x2.y)**2+(x1.z-x2.z)**2)