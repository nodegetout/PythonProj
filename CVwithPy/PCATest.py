from PIL import Image
from numpy import *
from pylab import*
from imtools import *
import PCA

imlist = get_imlist('imlist/')

im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)
gray()
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')
#perform PCA
V,S,immean = PCA.pca_book(immatrix)
#figure()
subplot(2,4,1)
imshow(immean.reshape(m,n,-1))
for i in range(imnbr-1):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n,-1))

show()