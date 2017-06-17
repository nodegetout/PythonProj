import cv2
import numpy as np

"""draw the flow"""
def draw_flow(im,flow,step=16):
    """"""
    h,w = im.shape[:2]
    y,x = np.mgrid[step/2:h:step,step/2:w:step].reshape(2,-1)
    fx,fy = flow[y,x].T

    lines = np.vstack([x,y,x+fx,y+fy]).T.reshape(-1,2,2)
    lines = np.int32(lines)

    vis = cv2.cvtColor(im,cv2.COLOR_GRAY2BGR)
    for (x1,y1),(x2,y2) in lines:
        cv2.line(vis,(x1,y1),(x2,y2),(0,255,0),1)
        cv2.circle(vis,(x1,y1),1,(0,255,0),-1)
    
    return vis


#the main video capture segment
cap = cv2.VideoCapture(0)
cap.set(CV_CAP_PROP_FRAME_WIDTH,640)
cap.set(CV_CAP_PROP_FRAME_HEIGHT,360)
ret,im = cap.read()
prev_gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

while True :
    ret,im = cap.read()
    cap.set(CV_CAP_PROP_FRAME_WIDTH,640)
    cap.set(CV_CAP_PROP_FRAME_HEIGHT,360)
    print ret
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    #flow = cv2.calcOpticalFlowFarneback(prevgray, gray, 0.5, 3, 15, 3, 5, 1.2, 0)
    flow = cv2.calcOpticalFlowFarneback(prev_gray,gray,0.5,3,15,3,5,1.2,0)
    prev_gray = gray

    cv2.imshow('Optical Flow',draw_flow(gray,flow))
    if cv2.waitKey(10) == 27:
        break