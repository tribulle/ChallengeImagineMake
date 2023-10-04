import math
import numpy as np


class point:
    """
    Cette classe permet de définir des points dans l'espace (en récupérant la sortie du système)
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.y = 0 
    def set_xyz(self, list : list):
        self.x = list[0]
        self.y = list[1]
        self.z = list[2]


    def set_angle_dist(self,data : list):
        """
        dist : la distance retournée par du capteur
        theta : l'angle "horizontal" (l'angle de rotation du lidar)
        phi : l'angle "vertical" (celui du moteur supplémentaire)
        """
        dist = data[0]
        theta = data[1]
        phi = data[2]
        self.x = dist*math.cos(theta)*math.cos(phi)
        self.y = dist*math.sin(phi)*math.cos(theta)
        self.z = dist*math.sin(theta)
    
    def afficher_point(self):
        print("X : "+str(self.x) + " Y : "+str(self.y) + " Z : "+str(self.z))


