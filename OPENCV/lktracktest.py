import lktrack
import cv2

imnames = ['test01.jpg','test02.jpg','test03.jpg','test04.jpg']

im = cv2.imread('./OPENCV/test.jpg',1)
for name in imnames:
    cv2.imwrite('./OPENCV/'+name,im)
    print name

lkt = lktrack.LKTracker(imnames)

lkt.detect_points()
#lkt.draw()
for i in range(len(imnames)-1):
    lkt.track_points()
    lkt.draw()
    cv2.imwrite('./OPENCV/traked'+lkt.imnames[i],lkt.image[i])