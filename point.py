import math

"""
Cette classe permet de définir des points dans l'espace (en récupérant la sortie du système)
"""
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.y = 0 
    def set(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    """
    dist : la distance retournée par du capteur
    theta : l'angle "horizontal" (l'angle de rotation du lidar)
    phti : l'angle "vertical" (celui du moteur supplémentaire)
    """
    def set_angle_dist(self,dist,theta,phi):
        self.x = dist*math.cos(theta)*math.sin(phi)
        self.y = dist*math.sin(phi)*math.sin(theta)
        self.z = dist*math.cos(theta)

