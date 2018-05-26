import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frames = []
while True:
    ret, im = cap.read()
    cv2.imshow('video capture',im)
    frames.append(im)
    if cv2.waitKey(10) == 27:
        break

frames = np.array(frames)
print im.shape
print frames.shape
    