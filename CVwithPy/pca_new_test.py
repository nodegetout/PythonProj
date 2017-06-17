from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from pca_new import pca
from PCA import pca_book

imX = np.array(Image.open('CVwithPy/test.jpg').convert('L'))
n,m = imX.shape[0:2]
points = []
for i in range(n):
    for j in range(m):
        if imX[i,j] < 128:
            points.append([float(j),float(n)-float(i)])
imX = np.mat(points).T
print 'im_X=',imX,'shape=',imX.shape

low_X,EV_main,mean_X = pca(imX)
recon_X = np.dot(EV_main,low_X) + mean_X
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(imX[0].A[0],imX[1].A[0],s=1,alpha=0.5)
ax.scatter(recon_X[0].A[0], recon_X[1].A[0],marker='o',s=100,c='blue',edgecolors='white')
plt.show()