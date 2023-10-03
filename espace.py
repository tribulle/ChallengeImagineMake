import point
import maille
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np
"""
Cette classe permet de définir l'ensemble des points de l'espace
"""

class espace:
    def __init__(self):
        self.points= []
    
    """
    A l'aide du jeu de données on place les points
    """
    def init_points(self,data):
        for i in range(len(data)):
            p = point.point()
            p.set_angle_dist(data[i])
            self.points.append(p)

    """
    Permet d'afficher à l'aide de matplotlib les points en 3D
    """
    def afficher(self):
        plt.figure(figsize=(100,100))
        axes = plt.axes(projection="3d")

        for i in self.points :
            axes.scatter(i.x,i.y,i.z)

        plt.show()

    """
    Retourne le nuage de points au format np.array([np.array([x,y,z]),...])
    afin d'être compatible avec la fonction mesh
    """
    def return_xyz(self):
        array = np.empty((len(self.points),3))
        for i in range(len(self.points)) :
            array[i][0] = self.points.x
            array[i][1] = self.points.y
            array[i][2] = self.points.z
        return array
    