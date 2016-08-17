# trying to import sys and PIL/image
import sys
from PIL import Image

# opens image file.
def open(argv):
    if len(argv)<=1:
        print "missing image filename"
        sys.exit(1)
    img = Image.open(argv[1])
    img = img.convert("L") # make greyscale if not already (luminance)
    return img




# gets pixels in a way that properly handles edge pixels
def getpixel(img,x,y):
    width, height = img.size
    if x<0:
        x=0
    elif x>=width:
        x=width-1
    if y<0:
        y=0
    elif y>=height:
        y=height-1
    pix=img.load()
    return pix[x,y]


# gets the values for the pixel at (x,y) and the 8 pixels around it.
def region3x3(img,x,y):
    p1=getpixel(img,x,y)
    p2=getpixel(img,x,y-1)
    p3=getpixel(img,x+1,y-1)
    p4=getpixel(img, x+1,y)
    p5 = getpixel(img, x + 1, y+1)
    p6 = getpixel(img, x , y + 1)
    p7 = getpixel(img, x + 1, y + 1)
    p8 = getpixel(img, x -1, y)
    p9 = getpixel(img, x -1, y-1)

    data=[p1,p2,p3,p4,p5,p6,p7,p8,p9]
    return data

# filter function that allows for input of any function
def filter(img,f):
    width, height = img.size
    #making duplicate image to save original
    imgdup=img.copy()
    #loading matrix for original
    m1 = img.load()
    #loading matrix for duplicate
    pixels = imgdup.load()
    #iterating through columns first and then rows
    for x in range(width):
        for y in range(height):
           r=region3x3(img,x,y)
           pixels[x,y]=f(r)
    return imgdup

