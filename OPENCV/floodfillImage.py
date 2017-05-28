import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread("./OPENCV/bookexampleimg.png",1)
plt_originim = Image.open("./OPENCV/bookexampleimg.png")
#get the image width and height
h,w = im.shape[:2]

#flood fill example
diff = (6,6,6)
mask = np.zeros((h+2,w+2),np.uint8)
floodfill = cv2.floodFill(im,mask,(10,10),(255,255,0),diff,diff)

"""使用pyplot显示对比图像"""
plt_im = cv2.cvtColor(floodfill[1],cv2.COLOR_BGR2RGB)
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(plt_im)
plt.subplot(122)
plt.imshow(plt_originim)
plt.show()

#write the result into a jpg image file
cv2.imwrite("./OPENCV/floodfill result.jpg",floodfill[1])

#cv2 image show
while True:
    cv2.imshow("the flood fill image",floodfill[1])
    if cv2.waitKey(10) == 27:
        break


