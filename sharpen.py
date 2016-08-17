import sys
from filter import *


# define function laplace here
def laplace(data):
    lap=data[3]+data[7]+data[5]+data[1]-4*data[0]
    return lap

# takes the original and the edge image, returns a new images whose pixels p[x,y]=A[x,y]-B[x,y]
def minus(A, B):
        width, height = img.size
        # makes copy of A to change
        p1 = A.copy()
        p2 = p1.load()
        # loads A image
        Am = A.load()
        # loads B image
        Bm = B.load()
        # iterating through columns first and then rows
        for x in range(width):
            for y in range(height):
                p2[x,y]=Am[x,y] - Bm[x, y]
        return p1

img = open(sys.argv)
img.show()
edges = filter(img, laplace)
newim=minus(img,edges)
newim.show()