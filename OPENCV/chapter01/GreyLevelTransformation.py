from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

with Image.open("./OPENCV/ImageData/test.jpg") as img:
    im = np.array(img.convert('L'))
    img1 = Image.fromarray(im)
    im = 255 - im
    img2 = Image.fromarray(im)  
    im = (100.0/255)*im+100
    img3 = Image.fromarray(im)
    im = 255*(im/255.0)**2
    img4 = Image.fromarray(im)   
    # print("im min :" ,im.min() , "max :" , im.max())
    plt.subplot(151)
    plt.imshow(img)
    plt.title("origin image")
    plt.subplot(152)
    plt.imshow(img1)
    plt.title("inverse image")
    plt.subplot(153)
    plt.imshow(img2)
    plt.title("inverse image")
    plt.subplot(154)
    plt.imshow(img3)
    plt.title("inverse image")
    plt.subplot(155)
    plt.imshow(img4)
    plt.title("inverse image")
    plt.show()