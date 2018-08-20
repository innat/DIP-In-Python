# importing necessary packages
from skimage import color
from skimage import exposure
import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# load the image
pic = imageio.imread('<image location>')
plt.figure(figsize = (6,6))
plt.imshow(pic);

# Convert the image to grayscale
img = color.rgb2gray(pic)

# outline kernel - used for edge detection
kernel = np.array([[-1,-1,-1],
                   [-1,8,-1],
                   [-1,-1,-1]])

# we use 'valid' which means we do not add zero padding to our image
edges = convolve2d(img, kernel, mode = 'valid')


# Adjust the contrast of the filtered image by applying Histogram Equalization
edges_equalized = exposure.equalize_adapthist(edges/np.max(np.abs(edges)),
                                              clip_limit = 0.03)

# plot the edges_clipped
plt.imshow(edges_equalized, cmap='gray')
plt.axis('off')
plt.show()
