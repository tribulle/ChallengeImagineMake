"""
Cette classe permet de définir des mailles (sets de 3 points)
pour créer une géométrie de base
"""

class maille:
    def __init__(self):
        self.points = []
    def add_point(self,point):
        self.points.append(point)
    