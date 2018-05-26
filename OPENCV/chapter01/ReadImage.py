import cv2
from PIL import Image
import matplotlib.pyplot as plt

pil_img = Image.open("./OPENCV/ImageData/test.jpg")
pil_img_L = pil_img.convert('L')

# cv2.imshow("Read Image",pil_img)
plt.subplot(121)
plt.imshow(pil_img)
plt.title("origin image")
plt.subplot(122)
plt.imshow(pil_img_L)
plt.title("gray scale image")
plt.show()