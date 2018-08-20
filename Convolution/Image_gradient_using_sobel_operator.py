
"""
Image Data Analysis Using Numpy & OpenCV
author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""


# importing necessary packages
from skimage import color
from skimage import exposure
import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# right sobel
sobel_x = np.c_[
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
]

# top sobel
sobel_y = np.c_[
    [1,2,1],
    [0,0,0],
    [-1,-2,-1]
]

ims = []
for i in range(3):
    sx = convolve2d(pic[:,:,i], sobel_x, mode="same", boundary="symm")
    sy = convolve2d(pic[:,:,i], sobel_y, mode="same", boundary="symm")
    ims.append(np.sqrt(sx*sx + sy*sy))

img_conv = np.stack(ims, axis=2).astype("uint8")

plt.figure(figsize = (6,5))
plt.axis('off')
plt.imshow(img_conv);
