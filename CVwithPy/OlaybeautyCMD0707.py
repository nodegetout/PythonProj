#import sys
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

def beauty(src,dst,center,radius,strength,m_Stride):
    #area to calculate
    left = 0 if (center[0]-radius<0) else (center[0]-radius)
    right  = (src.shape[1]-1) if (center[0]+radius>src.shape[1]) else (center[0]+radius)
    top = 0 if (center[1]-radius<0) else (center[1]-radius)
    bottom = (src.shape[0]-1) if (center[1]+radius>src.shape[0]) else (center[1]+radius)
    #radius
    powerRadius = radius*radius
    #print "left,right,top,bottom",left,right,top,bottom
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
                scaleFactor = 1.0 - float(strength)/100*scaleFactor
                posX = offsetX * scaleFactor + center[0]
                posY = offsetY * scaleFactor + center[1]
                if posX-1 < 0 :
                    posX = 0
                if posX+1 > src.shape[1]:
                    posX = src.shape[1]-1
                if posY-1 < 0 :
                    posY = 0
                if posY+1 > src.shape[0]:
                    posY = src.shape[0]-1
                cy = np.ceil(posY)
                fy = cy - 1
                cx = np.ceil(posX)
                fx = cx - 1
                w1=(cx-posX)*(cy-posY)  
                w2=(posX-fx)*(cy-posY)  
                w3=(cx-posX)*(posY-fy)  
                w4=(posX-fx)*(posY-fy)  
                if (posX-np.floor(posX)>1e-6 or posY-np.floor(posY)>1e-6):   
                    t=src[int(fy),int(fx)]*w1+src[int(fy),int(cx)]*w2+src[int(cy),int(fx)]*w3+src[int(cy),int(cx)]*w4  
                    t=np.ubyte(np.floor(t))
                    dst[j,i]= t
                else:
                    #dst[j][i] = 0
                    dst[j][i] = src[int(posY)][int(posX)]

def Whitize(src):
    i=j=0
    for i in range(src.shape[0:1]):
        for j in range(src.shape.pop[0:1]):
            print (j,i)

#parameters from cmd
#fileName,imgName,para1,para2,para3,para4,para5,para6=sys.argv
'''
'''
imgName = "testImage05.jpg"
para1 = 260
para2 = 430
para3 = 460
para4 = 460
para5 = 90
para6 = 30

im = cv2.imread(imgName)
origin = cv2.imread(imgName)
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
origin = cv2.cvtColor(origin,cv2.COLOR_BGR2RGB)
src = im.copy()
dst = im.copy()
center1 = (int(para1),int(para2))
beauty(src,dst,center1,para5,para6,2)
center2=(int(para3),int(para4))
src = dst.copy()
beauty(dst,src,center2,para5,para6,2)

Whitize(dst)
#blur
kernel = np.ones((1,1),np.float32)/1
dst = cv2.filter2D(src,-1,kernel)
dst = cv2.medianBlur(dst,3)
dst = cv2.bilateralFilter(dst,9, 15, 15)
#image write into disk
#im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
#dst = cv2.cvtColor(dst,cv2.COLOR_GRAY2RGB)
plt.subplot(121)
#origin[center1[1]+50][center1[0]-50] = (255,255,255)  
plt.imshow(origin)
plt.subplot(122)
plt.imshow(dst) 
plt.show()
#cv2.imwrite("./before.png", im, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])   
cv2.imwrite("./after.png", dst, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 
cv2.imwrite("./after1.png", dst, [int(cv2.IMWRITE_PNG_COMPRESSION), 9]) 