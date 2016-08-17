#trying to import sys and PIL/image
import sys
from PIL import Image

# define your flip function here
def flip(img):
    width, height = img.size
    #making duplicate image to save original
    imgdup=img.copy()
    #loading matrix for original
    m1 = img.load()
    #loading matrix for duplicate
    m2 = imgdup.load()
    #iterating through columns first and then rows
    for i in range(width):
        for j in range(height):
            m2[i,j]=m1[width-i-1, j]
    return imgdup

#checks for filename. If it is less than or equal to 1, prints an error message that filename is missing.
if len(sys.argv)<=1:
	print "missing image filename"
	sys.exit(1)

#reads in the filename, opens the image with filename.
filename = sys.argv[1]
img = Image.open(filename)
#converts image to black and white
img = img.convert("L")
img.show()

# call your flip function here
newim=flip(img)
#prints the new image from the flip function
newim.show()