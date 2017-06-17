from SimpleCV import Image
import cv2

img = Image("./OPENCV/test.jpg")
nutBolts = img.binarize().findBlobs()
nutBolts.image = img
nutBolts.show()

"""
while True:
    nutBolts.show()
    if cv2.waitKey(10) == 27:
        break
"""