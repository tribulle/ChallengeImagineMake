import math
import numpy as np

"""
Cette classe permet de définir des points dans l'espace (en récupérant la sortie du système)
"""
class point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.y = 0 
    def set_xyz(self, list):
        self.x = list[0]
        self.y = list[1]
        self.z = list[2]

    """
    dist : la distance retournée par du capteur
    theta : l'angle "horizontal" (l'angle de rotation du lidar)
    phi : l'angle "vertical" (celui du moteur supplémentaire)
    """
    def set_angle_dist(self,data):
        dist = data[0]
        theta = data[1]
        phi = data[2]
        self.x = dist*math.cos(theta)*math.cos(phi)
        self.y = dist*math.sin(phi)*math.cos(theta)
        self.z = dist*math.sin(theta)


