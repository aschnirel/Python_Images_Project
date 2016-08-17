import sys
from filter import *


# define function laplace here
def laplace(data):
    lap=data[3]+data[7]+data[5]+data[1]-4*data[0]
    return lap


img = open(sys.argv)
img.show()
edges = filter(img, laplace)
edges.show()