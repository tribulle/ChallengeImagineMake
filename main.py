import espace
import point
import random
import math
import MeshGenerator


def random_point():
    dist = 100 #random.randint(0,100)
    theta = random.uniform(0,math.pi*2)
    phi = random.uniform(0,math.pi*2)
    return [dist,theta,phi]

espace_in = espace.espace()
data = []
for i in range(2500):
    data.append(random_point())
#Le carré
data = []
data.append([-1,-1,-1])
data.append([-1,-1,1])
data.append([1,-1,-1])
data.append([-1,1,-1])

data.append([-1,1,1])
data.append([1,1,1])
data.append([1,1,-1])
data.append([1,-1,1])

espace_in.init_points(data,True)
#espace_in.afficher()

data_np = espace_in.return_xyz()

MeshGenerator.MeshGenerator(data_np)


