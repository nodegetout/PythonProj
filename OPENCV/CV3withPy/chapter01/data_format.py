import numpy as np
import cv2

img = np.zeros((3, 3), dtype=np.uint8)
print("create image array with numpy moudle")
print(img)
print(img.dtype)
print(img.shape)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print("convert image array into opencv3 image data")
print(img)
print(img.dtype)
print(img.shape)