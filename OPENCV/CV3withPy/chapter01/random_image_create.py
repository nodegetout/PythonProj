import cv2
import numpy as np
import os

random_byte_array = bytearray(os.urandom(120000))
flat_numpy_array = np.array(random_byte_array)

gray_image = flat_numpy_array.reshape(300, 400)
cv2.imwrite('./OPENCV/ImageData/output/random_gray.png', gray_image)

bgr_image = flat_numpy_array.reshape(100, 400, 3)
cv2.imwrite('./OPENCV/ImageData/output/random_color.png', bgr_image)