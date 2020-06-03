import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/profile.jpg', 0)
plt.imshow(
  cv2.Sobel(img, -1, 1, 0, ksize=5), cmap='gray'
)
plt.show()
plt.imshow(
  cv2.Sobel(img, -1, 0, 1, ksize=5), cmap='gray'
)
plt.show()
