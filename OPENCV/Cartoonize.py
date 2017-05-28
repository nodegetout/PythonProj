#move scripts into the OPENCV folder/finder
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

#application dealing with camera main-loop
#exit when user press ESC key
while True:
    if (not cap.isOpened()):
        break
    ret , im = cap.read()
    #resize the width and height
    # convert video stream into gray color space
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #median blur PS:the size must be a odd number
    median_blur = cv2.medianBlur(gray,9)
    #Laplacian
    edge = cv2.Laplacian(median_blur,cv2.CV_8U,5)
    #threshold mask
    mask = cv2.threshold(edge,8,255,cv2.THRESH_BINARY_INV)
    #mask = cv2.threshold(mask[1],8,255,cv2.THRESH_BINARY_INV)
    #mask = cv2.threshold(mask[1],8,255,cv2.THRESH_BINARY_INV)
    #print mask
    #blur = cv2.GaussianBlur(im,(0,0),0)

    #colorize and cartoonify
    #smallSize = (im.shape[0],im.shape[1])
    #smallImg = cv2.Mat(smallSize,cv2.CV_8UC3)
    #smallImg = M(smallSize,cv2.CV_8UC3)
    smallSize = im.shape[0]/2,im.shape[1]/2,im.shape[2]
    #smallImg = np.zeros(smallSize,dtype=np.uint8)
    smallImg = np.reshape(im,smallSize,cv2.INTER_LINEAR)
    #smallImg.reshape()
    cv2.imshow('video capture test',smallImg)
    if cv2.waitKey(10) == 27:
        break
