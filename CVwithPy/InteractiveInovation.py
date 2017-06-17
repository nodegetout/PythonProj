from PIL import Image
from pylab import *

def InputPoints():
    im = array(Image.open('CVwithpy/test.jpg'))
    imshow(im)
    print('Please click 3 points')
    x = ginput(3)
    print('you clicked:',x)
    show()

InputPoints()