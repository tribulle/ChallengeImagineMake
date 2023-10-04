"""
Classe qui permet de définir des figures de base pour nos tests
"""

import random
import math

def random_point(rayon: int):
    dist = rayon #random.randint(0,100)
    theta = random.uniform(0,math.pi*2)
    phi = random.uniform(0,math.pi*2)
    return [dist,theta,phi]

class figure_test:
    @staticmethod
    def cube(taille: int):
        data = []
        data.append([-taille,-taille,-taille])
        data.append([-taille,-taille,taille])
        data.append([taille,-taille,-taille])
        data.append([-taille,taille,-taille])

        data.append([-taille,taille,taille])
        data.append([taille,taille,taille])
        data.append([taille,taille,-taille])
        data.append([taille,-taille,taille])
        return data
    
    @staticmethod
    def sphere(nb_points: int, rayon: int):
        data = []
        for i in range(nb_points):
            data.append(random_point(rayon))
        return data