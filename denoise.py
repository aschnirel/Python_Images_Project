# trying to import sys and PIL/image
import sys
from PIL import Image

# define your denoise function here
def denoise(img):
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
           pixels[x,y]=median(r)

    return imgdup

# takes the median of 9 pixels in 3x3 grid
def median(data):
    sort=sorted(data)
    medindex=len(sort)/2
    med=sort[medindex]
    return med

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



# checks for filename. If it is less than or equal to 1, prints an error message that filename is missing.
if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)

# reads in the filename, opens the image with filename.
filename = sys.argv[1]
img = Image.open(filename)
#converts image to black and white
img = img.convert("L")
img.show()

# call and print your blur function here
newim=denoise(img)
newim.show()