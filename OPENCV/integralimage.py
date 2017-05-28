#modules imports
import cv2
from PIL import Image
import matplotlib.pylab as plt
import numpy as np

#read the image
im = cv2.imread('./test.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#calculate integral image
intim = cv2.integral(gray)

#norm and save the image
normim = 255.0*intim/intim.max()
cv2.imwrite('integralresult.jpg',normim)

im1 = Image.open('./test.jpg')
im2 = np.array(Image.open('./integralresult.jpg').convert('L'))
m,n = im2.shape[0:2]

plt.figure()
ax = plt.subplot(121)
plt.imshow(im1)
plt.subplot(122)
plt.imshow(im2.reshape(m,-1))

plt.show()
