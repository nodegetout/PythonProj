import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
"""
im = cv2.imread('test.jpg',0)
#h,w = im.shape[:2]
print h,m

cv2.imshow('test.jpg',im)
"""
img = cv2.imread("test.jpg",1)
im = Image.open("test.jpg")

while True:
    #cv2.namedWindow("Imread Test Window")
    cv2.imshow("Imread Test Window",img)
    imRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    print 'cv2.imread',img.shape
    print 'Image.open' , im
    #im = img[:, :, (2, 1, 0)] 
    plt.imshow(imRGB)
    plt.show("Pyplot Show Image")
    if cv2.waitKey(10) == 27:
        break


#img = Image.open("test.jpg")
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.imshow(img)
#plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
#plt.show()