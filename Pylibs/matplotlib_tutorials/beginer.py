import matplotlib.pyplot as plt
import numpy as np
"""chapter 5 tutorial"""
"""
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
"""
"""
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,20])
plt.show()
"""
"""
#sample numbers from 0 to 5 by a step of 0.2
t = np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.show()
"""
"""
# some math function sampler examples
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.,5.,0.1)
t2 = np.arange(0.,5.,0.02)

plt.figure(1)
plt.subplot(221)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2),'r--')

plt.show()
"""
import matplotlib.image as mpimg

im = mpimg.imread('./test.jpg')
lum_img = im[:,:,0]
im_plot = plt.imshow(lum_img)
plt.colorbar()
im_plot.set_cmap('spectral')
plt.colorbar()
plt.show()
