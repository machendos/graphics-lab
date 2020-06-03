from PIL import Image
from skimage import filters
from scipy import ndimage

# with SKImage
a = Image.open('../images/moon.jpg')
b = filters.sobel(a)
b = Image.fromarray(b)
b.show()
