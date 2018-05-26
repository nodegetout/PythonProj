from PIL import Image
import numpy as np

with Image.open("./OPENCV/ImageData/test.jpg") as img:
    im = np.array(img)
    print(im.shape)
    print(im.dtype)
    im = np.array(img.convert('L'))
    print(im.shape)
    print(im.dtype)