import numpy as np 
import scipy.misc, math
from PIL import Image

# equalsing
started = Image.open('../images/girlface.bmp')
imageArray = np.asarray(started)
fl = imageArray.flatten()
hist, bins = np.histogram(imageArray, 256, [0,255])
cdf = hist.cumsum()
cdfNoZeroes = np.ma.masked_equal(cdf, 0)
numeratorCdfNoZeroes = (cdfNoZeroes - cdfNoZeroes.min())*255
denominatorCdfNoZeroes = (cdfNoZeroes.max() - cdfNoZeroes.min())
cdfNoZeroes = numeratorCdfNoZeroes / denominatorCdfNoZeroes
cdf = np.ma.filled(cdfNoZeroes, 0).astype('uint8')
im2 = cdf[fl]
im3 = np.reshape(im2, imageArray.shape)
im4 = Image.fromarray(im3)
im4.show()
