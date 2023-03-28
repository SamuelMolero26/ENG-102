#By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jackson Barge
#               Brandon Becerra
#               Christian Flewelling
#               Samuel Molero
# Section:      CRN 506
# Assignment:   Lab 3.16 team
# Date:         09 09 2022
#

import math
import operator
import numpy as np


def add(a, b):
    return tuple(map(operator.add, a, b))

def sub(a, b):
    return tuple(map(operator.sub, a, b))

def sc_mul(sc, tup):
    return tuple([sc * i for i in tup])

def compute_lerp(time, point1, point2):
    # i am storing time in these points, honestly a namedtuple with the point and time
    # separately would be nicer, but ehhhhhh
    #point1 = (8.0, 6.0, 7.0, 12.0)
    #point2 = (-5.0, 30.0, 9.0, 85.0)

    vel = sc_mul(1/(point2[3] - point1[3]), sub(point2[:3], point1[:3]))

    start = sub(point1[:3], sc_mul(point1[3], vel))

    return add(start, sc_mul(time, vel)) + (time,)


t1 = float(input('Enter time 1: '))
x1 = float(input('Enter the x position of the object at time 1: '))
y1 = float(input('Enter the y position of the object at time 1: '))
z1 = float(input('Enter the z position of the object at time 1: '))
p1 = (x1, y1, z1, t1)

t2 = float(input('Enter time 2: '))
x2 = float(input('Enter the x position of the object at time 2: '))
y2 = float(input('Enter the y position of the object at time 2: '))
z2 = float(input('Enter the z position of the object at time 2: '))
p2 = (x2, y2, z2, t2)

print()

def cl(x):
  if math.fabs(x) < 0.00001:
    return math.fabs(x)
  return x

step = (t2-t1)/4
for t in np.arange(t1, t2 + step, step):
  pt = compute_lerp(t, p1, p2)
  print('At time {:.2f} seconds the object is at ({:.3f}, {:.3f}, {:.3f})'.format(t, cl(pt[0]), cl(pt[1]), cl(pt[2])))
