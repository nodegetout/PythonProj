import cv2
from PIL import Image
import matplotlib.pyplot as plt

im = cv2.imread('./test.jpg',0)
plt.imshow(im)
plt.show()