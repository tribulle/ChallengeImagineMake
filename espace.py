import point
import maille
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np


class espace:
    """
    Cette classe permet de définir l'ensemble des points de l'espace
    """
    def __init__(self):
        self.points= []
    
    
    def init_points(self,data : list,mode=False):
        """
        A l'aide du jeu de données on place les points
        """
        for i in range(len(data)):
            p = point.point()
            if(mode):
                p.set_xyz(data[i])
            else:
                p.set_angle_dist(data[i])
            self.points.append(p)

    
    def afficher(self):
        """
        Permet d'afficher à l'aide de matplotlib les points en 3D
        """
        plt.figure(figsize=(100,100))
        axes = plt.axes(projection="3d")

        for i in self.points :
            axes.scatter(i.x,i.y,i.z)

        plt.show()

    
    def return_xyz(self):
        """
        Retourne le nuage de points au format np.array([np.array([x,y,z]),...])
        afin d'être compatible avec la fonction mesh
        """
        array = np.empty((len(self.points),3))
        for i in range(len(self.points)) :
            array[i][0] = self.points[i].x
            array[i][1] = self.points[i].y
            array[i][2] = self.points[i].z
        return array
    