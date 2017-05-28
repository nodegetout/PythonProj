import cv2
from PIL import Image
import matplotlib.pyplot as plt

im = cv2.imread("./OPENCV/test.jpg",1)
plt_im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
plt.imshow(plt_im)
plt.show()