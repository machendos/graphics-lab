from PIL import Image
import scipy.ndimage as sc
import scipy.misc as sm

# median filter
started = Image.open('../images/lena_noisy.png')
b = sc.filters.median_filter(
  started, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0
)
b = Image.fromarray(b)
b.show()
