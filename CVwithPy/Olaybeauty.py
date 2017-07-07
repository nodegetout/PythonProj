import math
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters
import os
import cv2
import cv2.cv as cv

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
    #print i,j
    for i in range(left,right):
        offsetX = i - center[0]
        for j in range(top,bottom):
            offsetY = j - center[1]
            XY = offsetX*offsetX+offsetY*offsetY
            if XY <= powerRadius:
                scaleFactor = 1.0 - float(XY)/float(powerRadius)
                scaleFactor = 1 - float(strength)/100*scaleFactor
                '''
                posX = int(offsetX * scaleFactor) + center[0]
                posY = int(offsetY * scaleFactor) + center[1]
                '''
                posX = offsetX * scaleFactor + center[0]
                posY = offsetY * scaleFactor + center[1]
                y = float(i)*scaleFactor
                x = float(j)*scaleFactor
                if posX < 0 :
                    posX = 0
                if posX+1 > src.shape[1]:
                    posX = src.shape[1]-1
                if posY < 0 :
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
                    #print t
                    dst[j,i]=t
                else:
                    dst[j][i] = src[int(posY)][int(posX)]
                    '''
                #t=src[int(fy),int(fx)]*w1+src[int(fy),int(cx)]*w2+src[int(cy),int(fx)]*w3+src[int(cy),int(cx)]*w4  
                #t=np.ubyte(np.floor(t))
                #dst[j][i] = t
                #dst[j][i] = src[int(posY)][int(posX)]
                #'''
            
    #dst = cv2.resize(dst,(dst.shape[0],dst.shape[1]),interpolation=cv2.INTER_CUBIC)
    #box_data = np.array(dst)
    #box_data = dst[:,bottom,right]
    #eara = cv.rect()
    #cv.SetImageROI(dst,(center[0], center[1], radius*2, radius*2))
    #plt.show(box_data)
def whitize(src,dst,beta):
    h,w,c = src.shape
    #print("image width:",w,",image height:",h)
    i=j=0
    for i in range(0,w):
        for j in range(0,h):
            up0 = math.log(src[j][i][0]*(beta-1)+1)
            up1 = math.log(src[j][i][1]*(beta-1)+1)
            up2 = math.log(src[j][i][2]*(beta-1)+1)
            dst[j][i][0] = up0/math.log(beta)
            dst[j][i][1] = up1/math.log(beta)
            dst[j][i][2] = up2/math.log(beta)
    return dst

#im = np.array(Image.open('CVwithPy/test.jpg').convert('L'))
im = cv2.imread("testImage05.jpg")
origin = cv2.imread("testImage05.jpg")
#im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY);
#im2 = filters.gaussian_filter(im,5)
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
origin = cv2.cvtColor(origin,cv2.COLOR_BGR2RGB)
src = im.copy()
dst = im.copy()
print "im",im.shape
print "src",src.shape
print "dst",dst.shape
#center(x,y)
#center1 = (340,480)
center1 = (260,430)
#center = (415,368)
print "center",center1
#beauty(src,dst,center,radius,strength,m_strike)
beauty(src,dst,center1,60,30,10)
print("src id:",id(src))
print("dst id:",id(dst))
center2=(460,460)
src = dst.copy()
print("src copy id:",id(src))
print("dst copy id:",id(dst))
beauty(dst,src,center2,60,30,10)
#center3=(int(center1[0]*0.5+center2[0]*0.5),int(center1[1]*0.5+center2[1]*0.5))
#beauty(dst,dst,center3,60,5,1)
#smooth image
#src = dst.copy()
#Mopi(src,dst,value1,value2,p)
#Mopi(dst,dst,3,4,50)
#dst = whitize(dst,dst,5)
dst = cv2.resize(dst,(dst.shape[0],dst.shape[1]),interpolation=cv2.INTER_LINEAR)
#dst = cv2.resize(dst,None,fx=2, fy=2,interpolation=cv2.INTER_LINEAR)
#dst = cv2.bilateralFilter(dst,16,16, 256, 32)
kernel = np.ones((1,1),np.float32)/1
dst = cv2.filter2D(src,-1,kernel)
#src = cv2.cv.CreateImage(dst,dst,dst.channels())
#cv2.cv.Smooth(src,dst,cv2.cv.CV_GAUSSIAN_5x5)
#kernel_erode = np.ones((5,5),np.uint8)
#dst = cv2.erode(dst,kernel,1)
#Mopi(dst,dst,3,4,50)
plt.subplot(121)
#origin[center1[1]+50][center1[0]-50] = (255,255,255)  
plt.imshow(origin)
plt.subplot(122)
plt.imshow(dst) 
plt.show()
#image write into disk
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)
cv2.imwrite("./before.png", im, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])   
cv2.imwrite("./after.png", dst, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 