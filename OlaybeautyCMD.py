#support the simple chinese
#coding=utf-8

#import modules
#import sys
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

#
def beauty(src,dst,center,radius,strength,m_strike):
    #area to calculate
    print("src function id:",id(src))
    print("dst function id:",id(dst))
    left = 0 if (center[0]-radius<0) else (center[0]-radius)
    right  = (src.shape[1]-1) if (center[0]+radius>src.shape[1]) else (center[0]+radius)
    top = 0 if (center[1]-radius<0) else (center[1]-radius)
    bottom = (src.shape[0]-1) if (center[1]+radius>src.shape[0]) else (center[1]+radius)
    #power radius
    powerRadius = radius*radius
    #print "left,right,top,bottom",left,right,top,bottom
    '''stuff above is good'''
    #implement the scale
    i = left
    j = top
    cout = 0
    #print i,j
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

#
# 
def Mopi(src,dst,value1,value2,p):
    #
    dx = value1*5
    fc = value1*12.5
    temp1 = cv2.bilateralFilter(dst,dx, fc, fc)
    temp2 = (temp1-dst+128)
    temp3 = cv2.GaussianBlur(temp2,(2 * value2 - 1, 2 * value2 - 1),0,0)
    temp4 = dst + 2 * temp3 - 255;
    dst = (dst*(100 - p) + temp4*p) / 100;
# 
#
#fileName,imgName,para1,para2,para3,para4=sys.argv
imgName = "test.png"
para1 = 260
para2 = 430
para3 = 460
para4 = 460
im = cv2.imread(imgName)
origin = cv2.imread(imgName)
im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
origin = cv2.cvtColor(origin,cv2.COLOR_BGR2GRAY)
src = im.copy()
dst = im.copy()
print("src id:",id(src))
print("dst id:",id(dst))
'''
print "im",im.shape
print "src",src.shape
print "dst",dst.shape
'''
center = (int(para1),int(para2))
beauty(dst,dst,center,90,40,1)
center = (int(para3),int(para4))
#src = dst.copy()
beauty(dst,dst,center,90,40,1)
print("src copy id:",id(src))
print("dst copy id:",id(dst))

plt.subplot(121)
plt.imshow(origin)
plt.subplot(122)
plt.imshow(dst) 
plt.imshow(dst)
plt.show()

#print("Hello World")
#dst = cv2.bilateralFilter(dst, 10, 10*2,10/2)
dst = cv2.bilateralFilter(dst,9,9, 81, 18)
#image write into disk
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
#cv2.imwrite("./before.png", im, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])   
#cv2.imwrite("./after.png", dst, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 