#coding = utf-8
#move scripts into the OPENCV folder/finder
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

print "完成了视频的捕捉"

#application dealing with camera main-loop
#exit when user press ESC key
while True:
    if (not cap.isOpened()):
        break
    ret , im = cap.read()
    #resize the width and height
    # convert video stream into gray color space
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #median blur PS:the size must be a odd number : return [retval,dst]
    median_blur = cv2.medianBlur(gray,9)
    #Laplacian  : return [retval,dst]
    edge = cv2.Laplacian(median_blur,cv2.CV_8U,5)
    #threshold mask : return [retval,dst]
    mask = cv2.threshold(edge,8,255,cv2.THRESH_BINARY_INV)
    #mask = cv2.threshold(mask[1],8,255,cv2.THRESH_BINARY_INV)
    #mask = cv2.threshold(mask[1],8,255,cv2.THRESH_BINARY_INV)
    #print mask
    #blur = cv2.GaussianBlur(im,(0,0),0)

    #colorize and cartoonify
    #smallSize = (im.shape[0],im.shape[1])
    #smallImg = cv2.Mat(smallSize,cv2.CV_8UC3)
    #smallImg = M(smallSize,cv2.CV_8UC3)

    #resize the video : notice that the shape is [height,width]
    smallSize = im.shape[1]/2,im.shape[0]/2,im.shape[2]
    smallImg = cv2.resize(mask[1],smallSize[:2],cv2.INTER_LINEAR)
    cv2.imshow('video capture test',smallImg)
    if cv2.waitKey(10) == 27:
        break
