import sys
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

def beauty(src,dst,center,radius,strength,m_strike):
    #area to calculate
    left = 0 if (center[0]-radius<0) else (center[0]-radius)
    right  = (src.shape[1]-1) if (center[0]+radius>src.shape[1]) else (center[0]+radius)
    top = 0 if (center[1]-radius<0) else (center[1]-radius)
    bottom = (src.shape[0]-1) if (center[1]+radius>src.shape[0]) else (center[1]+radius)
    #radius
    powerRadius = radius*radius
    print "left,right,top,bottom",left,right,top,bottom
    #implement the scale
    i = left
    j = top
    cout = 0
    print i,j
    for i in range(left,right):
        offsetX = i - center[0]
        for j in range(top,bottom):
            offsetY = j - center[1]
            XY = offsetX*offsetX+offsetY*offsetY
            if XY <= powerRadius:
                scaleFactor = 1.0 - float(XY)/float(powerRadius)
                scaleFactor = 1 - float(strength)/100*scaleFactor
                posX = int(offsetX * scaleFactor) + center[0]
                posY = int(offsetY * scaleFactor) + center[1]
                if posX < 0 :
                    posX = 0
                if posX > src.shape[1]:
                    posX = src.shape[1]-1
                if posY < 0 :
                    posY = 0
                if posY > src.shape[0]:
                    posY = src.shape[0]-1
                dst[j][i] = src[posY][posX]

def Mopi(src,dst,value1,value2,p):
    #
    dx = value1*5
    fc = value1*12.5
    temp1 = cv2.bilateralFilter(dst,dx, fc, fc)
    temp2 = (temp1-dst+128)
    temp3 = cv2.GaussianBlur(temp2,(2 * value2 - 1, 2 * value2 - 1),0,0)
    temp4 = dst + 2 * temp3 - 255;
    dst = (dst*(100 - p) + temp4*p) / 100;
    #dst.copyTo(image);


#parameters from cmd
fileName,imgName,para1,para2,para3,para4=sys.argv
im = cv2.imread(imgName)
origin = cv2.imread(imgName)
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
origin = cv2.cvtColor(origin,cv2.COLOR_BGR2RGB)
src = im.copy()
dst = im.copy()
center1 = (int(para1),int(para2))
beauty(src,dst,center1,60,40,10)
center2=(int(para3),int(para4))
src = dst.copy()
beauty(dst,src,center2,80,40,10)
#blur
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(src,-1,kernel)
#Mopi(src,dst,value1,value2,p)
Mopi(dst,dst,3,4,50)
dst = cv2.bilateralFilter(dst,9,9, 81, 18)
'''
plt.subplot(121)
plt.imshow(origin)
plt.subplot(122)
plt.imshow(dst) 
plt.show()
'''
#image write into disk
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
cv2.imwrite("./before.png", im, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])   
cv2.imwrite("./after.png", dst, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 