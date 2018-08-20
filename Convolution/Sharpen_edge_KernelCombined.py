
"""
Image Data Analysis Using Numpy & OpenCV
author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""

#importing necessary packages
from skimage import color
from skimage import exposure
import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

pic = imageio.imread('<image location>')
# Convert the image to grayscale
img = color.rgb2gray(img)

# apply sharpen filter to the original image
sharpen_kernel = np.array([[0,-1,0],
                           [-1,5,-1],
                           [0,-1,0]])
image_sharpen = convolve2d(img, sharpen_kernel, mode = 'valid')

# apply edge kernel to the output of the sharpen kernel
edge_kernel = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])
edges = convolve2d(image_sharpen, edge_kernel, mode = 'valid')

# apply normalize box blur filter to the edge detection filtered image
blur_kernel = np.array([[1,1,1],
                        [1,1,1],
                        [1,1,1]])/9.0;
denoised = convolve2d(edges, blur_kernel, mode = 'valid')

# Adjust the contrast of the filtered image by applying Histogram Equalization
denoised_equalized = exposure.equalize_adapthist(denoised/np.max(np.abs(denoised)),
                                                 clip_limit=0.03)
plt.imshow(denoised_equalized, cmap='gray')    # plot the denoised_clipped
plt.axis('off')
plt.show()
