from PIL import Image
import pylab as plt
import numpy as np

def pca(X,k=1):
    d,n = X.shape
    mean_X = np.mean(X,axis=1)
    print 'mean_X=',mean_X
    X = X - mean_X
    C = np.dot(X,X.T)
    e,EV = np.linalg.eig(np.mat(C))
    print 'C=',C
    e_idx = np.argsort(-e)[:k]
    EV_main = EV[:,e_idx]
    low_X = np.dot(EV_main.T,X)
    return low_X,EV_main,mean_X