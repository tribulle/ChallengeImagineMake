import espace
import point
import random
import math
import MeshGenerator
import figures_test


espace_in = espace.espace()
data = figures_test.figure_test.sphere(2500,100)
espace_in.init_points(data,False)
#espace_in.afficher()

data_np = espace_in.return_xyz()

MeshGenerator.MeshGenerator(data_np)


