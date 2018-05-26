#import modules
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from imtools import get_imlist
import os

impaths = get_imlist('imlist/')
im = np.array(Image.open(impaths[0]).convert('L'))
m,n = im.shape[0:2]
print 'm,n = ' , m , n

X = np.mat([np.array(Image.open(impath)).flatten() for impath in impaths]).T
print 'X.shape=',X.shape

def pca(X):
    dim,num_data = X.shape
    print dim,num_data
    mean_X = X.mean(axis=0)
    X = X - mean_X

    M = np.dot(X.T,X)
    e,EV = np.linalg.eigh(M)
    print 'e=', e.shape,e
    print 'EV=', EV.shape,EV

    tmp = np.dot(X,EV)
    print 'tmp=',tmp
    V = tmp[::-1]
    print 'V=',V.shape,V

    for i in range(EV.shape[1]):
        V[:,i] /= np.linalg.norm(EV[:,i])

    #print '(V,EV,mean_X)',V,EV,mean_X

    return V,EV,mean_X

#pca(X)
V,EV,mean_X = pca(X)
plt.gray()
plt.subplot(241)
plt.imshow(im.reshape(285,-1))
for i in range(7):
    plt.subplot(2,4,i+2)
    print 'V[',i,']=',V[i]
    plt.imshow(V[i].reshape(285,-1))
plt.show()