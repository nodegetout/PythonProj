from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def im_resize(img_array,size):
    pil_img = Image.fromarray(uint8(img_array))
    return np.array(pil_img.resize(size))