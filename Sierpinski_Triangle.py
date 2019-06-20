import numpy as np
import pylab
from random import uniform
from random import randint

def midpoint(point1, point2):
    return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]

# three points f the triangle chosen at random 
v1 = [uniform(0,2),uniform(0,2)]
v2 = [uniform(0,2),uniform(0,2)]
v3 = [uniform(0,2),uniform(0,2)]

curr_point = v1 # our initial value for the chaos game
# Plot 5000 points
for _ in range(5000):
    # choose a triangle vertex at random
    val = randint(0,2)
    if val == 0:
        curr_point = midpoint(curr_point, v1)
    if val == 1:
        curr_point = midpoint(curr_point, v2)
    if val == 2:
        curr_point = midpoint(curr_point, v3)
    # plot the new current point
    pylab.plot(curr_point[0],curr_point[1],'m.',markersize=2)

pylab.show()
