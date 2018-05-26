#coding = utf-8
#move scripts into the OPENCV folder/finder
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

print("完成了视频的捕捉")

#application dealing with camera main-loop
#exit when user press ESC key
while True:
    if (not cap.isOpened()):
        break
    ret, im = cap.read()
    #resize the width and height
    # convert video stream into gray color space
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #median blur PS:the size must be a odd number : return [retval,dst]
    median_blur = cv2.medianBlur(gray, 9)
    #Laplacian  : return [retval,dst]
    edge = cv2.Laplacian(median_blur, cv2.CV_8U, 5)
    #threshold mask : return [retval,dst]
    mask = cv2.threshold(edge, 8, 255, cv2.THRESH_BINARY_INV)
    #show the image
    cv2.imshow('video capture test', mask[1])
    #char keypress = cv2.waitKey(20)
    if cv2.waitKey(10) == 27:
        break