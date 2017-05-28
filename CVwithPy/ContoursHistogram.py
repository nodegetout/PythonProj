from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#from Tkinter

plt.hold(True)
#plt.figure(1)
plt.title('Plotting:"test.jpg"')
img = Image.open('test.jpg')
im = img.convert('L')
fig = plt.figure(1)
#original image
#plt.subplot(221)
ax = fig.add_subplot(221)
ax.imshow(img)
ax.set_title("The Original Image")
#plt.plot(im)
#grayed image
#plt.subplot(222)
#fig.gray()
ax = fig.add_subplot(222)
#fig = plt.gray()
#ax.imshow(fig)
ax.set_title("The Grey Image")
#contoured image
#plt.subplot(223)
ax = fig.add_subplot(223)
ax.contour(im,origin='image')
#ax.plot(fig3)
ax.set_title("The Contour Image")
#histogram image
#plt.subplot(224)
ax = fig.add_subplot(224)
#ax.hist(im.flatten(),128)
#ax.set_title("The hist Image")
plt.show()