import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = cv2.imread("./OPENCV/bookexampleimg.png",1)
plt_originim = Image.open("./OPENCV/bookexampleimg.png")
#get the image width and height
h,w = im.shape[:2]
#down sampler
im_lower = cv2.pyrDown(im)
#gray image
gray = cv2.cvtColor(im_lower,cv2.COLOR_RGB2GRAY)
#detection the feature point
#s = cv2.SURF(400)
surf = cv2._getRawKeypoints()
mask = np.uint8(np.ones(gray.shape))
keypoints = surf.detect(gray,mask)
#show the key points
vis = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)

for k in keypoints[::10]:
    cv2.Circle(vis,(int(k.pt[0]),int(k.pt[1]),2,(0,255,0),-1))
    cv2.Circle(vis,(int(k.pt[0]),int(k.pt[1]),int(k.size),(0,255,0),2))

"""使用pyplot显示对比图像"""

plt_im = cv2.cvtColor(vis,cv2.COLOR_BGR2RGB)
plt_originim = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(plt_im)
plt.subplot(122)
plt.imshow(plt_originim)
plt.show()


#write the result into a jpg image file
cv2.imwrite("./OPENCV/floodfill result.jpg",vis)

#cv2 image show
while True:
    cv2.imshow("the flood fill image",vis)
    if cv2.waitKey(10) == 27:
        break


