import cv2
import skimage as s
import scipy.ndimage as sc
import numpy as np
from matplotlib import pyplot as plt

# prewitt mask
moon = cv2.imread('../images/moon.jpg', 0)
img = s.img_as_int(moon)
prewittVert = np.array(
  [[-1,0,1],[-1,0,1],[-1,0,1]], dtype='float64'
)
prewittVertOut = s.img_as_ubyte(sc.convolve(img, prewittVert, mode='constant', cval=0.0))
plt.imshow(prewittVertOut, cmap='gray')
plt.show()
