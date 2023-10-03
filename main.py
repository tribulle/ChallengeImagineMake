import espace
import point
import random
import math


def random_point():
    dist = 100 #random.randint(0,100)
    theta = random.uniform(0,math.pi*2)
    phi = random.uniform(0,math.pi*2)
    return [dist,theta,phi]

espace_in = espace.espace()
data = []
for i in range(500):
    data.append(random_point())

espace_in.init_points(data)
espace_in.afficher()