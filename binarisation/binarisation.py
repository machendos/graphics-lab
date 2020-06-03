from PIL  import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *
from skimage import data

# Binarisation
started = data.page()
plt.imshow(started, cmap = cm.gray)
plt.show()
imageArray = np.zeros(shape(started)).astype('uint8')
threshold = 90

imageArray[started < threshold] = 0
imageArray[started >= threshold] = 255
plt.imshow(imageArray, cmap = cm.gray)
plt.show()
