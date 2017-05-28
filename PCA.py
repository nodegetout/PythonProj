from PIL import Image
from pylab import *
from numpy import *

def pca_book(X):
    num_data,dim = X.shape
    mean_X = X.mean(axis = 0)
    X = X - mean_X
    if dim > num_data:
        M=dot(X,X.T)
        e,EV = linalg.eigh(M)
        temp = dot(X.T,EV).T
        V = temp[::-1]
        S = sqrt(e)[::-1]
        #norm
        for i in range(V.shape[1]):
            V[:,i] /= linalg.norm(V[:,i])
    else:
        U,S,V = linalg.svd(X)
        V = V[:num_data]
    return V,S,mean_X