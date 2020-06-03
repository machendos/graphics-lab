from PIL import Image
from pylab import *

# Histogram
image = Image.open('../images/girlface.bmp').convert('L')

imgArray = array(image)
hist(imgArray.flatten(), 128)
show()
