import Point
import random
import math


def random_pos():
    dist = random.randint(0,100)
    angle1 = random.uniform(0,2*math.pi)
    angle2 = random.uniform(0,2*math.pi)
    return [dist,angle1,angle2]

