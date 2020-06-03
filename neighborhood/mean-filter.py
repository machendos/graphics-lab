from PIL import Image
import scipy.ndimage as sc
import numpy as np

# mean filter
started = Image.open('../images/profile.png').convert('L')
k = np.ones((5,5))/25
b = sc.filters.convolve(started,k)
b = Image.fromarray(b)
b.show()
