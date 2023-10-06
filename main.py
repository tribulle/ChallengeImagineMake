import espace
import point
import random
import math
import MeshGenerator
import figures_test



espace_in = espace.espace()
data = figures_test.figure_test.sphere(2500,100)
data = figures_test.figure_test.cube(1)
espace_in.init_points(data,True)
#espace_in.afficher()

data_np = espace_in.return_xyz()

MeshGenerator.MeshGenerator(data_np)


