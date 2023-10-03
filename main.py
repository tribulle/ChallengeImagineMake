import espace
import point
import random
import math


def random_point():
    dist = random.randint(0,100)
    theta = random.uniform(0,math.pi*2)
    phi = random.uniform(0,math.pi*2)
    return [dist,theta,phi]

espace_in = espace()
data = []
for i in range(100):
    data.append(random_point())

espace_in.init_points(data)