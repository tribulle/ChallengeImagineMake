import point
import maille
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
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
    