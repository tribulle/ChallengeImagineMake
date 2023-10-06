"""
Classe qui permet de définir des figures de base pour nos tests
"""

import random
import math
import random

def random_point(rayon: int):
    dist = rayon 
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

    def cubeRD(taille: int, random_factor: float):
        points = []

        for _ in range(taille):
            # Choisissez une face aléatoire du cube
            face = random.choice(['front', 'back', 'left', 'right', 'top', 'bottom'])

            if face == 'front':
                x = random.uniform(-0.5, 0.5)
                y = random.uniform(-0.5, 0.5)
                z = 0.5 + random.uniform(-1,1)*random_factor
            elif face == 'back':
                x = random.uniform(-0.5, 0.5)
                y = random.uniform(-0.5, 0.5)
                z = -0.5+ random.uniform(-1,1)*random_factor
            elif face == 'left':
                x = -0.5+ random.uniform(-1,1)*random_factor
                y = random.uniform(-0.5, 0.5)
                z = random.uniform(-0.5, 0.5)
            elif face == 'right':
                x = 0.5+ random.uniform(-1,1)*random_factor
                y = random.uniform(-0.5, 0.5)
                z = random.uniform(-0.5, 0.5)
            elif face == 'top':
                x = random.uniform(-0.5, 0.5)
                y = 0.5+ random.uniform(-1,1)*random_factor
                z = random.uniform(-0.5, 0.5)
            elif face == 'bottom':
                x = random.uniform(-0.5, 0.5)
                y = -0.5+ random.uniform(-1,1)*random_factor
                z = random.uniform(-0.5, 0.5)

            points.append([x, y, z])

        return points
    
    @staticmethod
    def sphere(nb_points: int, rayon: int):
        data = []
        for i in range(nb_points):
            data.append(random_point(rayon))
        return data