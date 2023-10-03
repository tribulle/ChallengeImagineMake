import point
import maille
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
            p = point()
            p.set_angle_dist(data[i])
            self.points.append(p)

    