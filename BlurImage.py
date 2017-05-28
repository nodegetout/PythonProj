from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import filters
import os


im = np.array(Image.open('test.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
plt.imshow(im) 
plt.show()
