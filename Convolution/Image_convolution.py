
"""
Image Data Analysis Using Numpy & OpenCV
author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""

# importing necessary packages
import numpy as np
import imageio
import matplotlib.pyplot as plt
from scipy.signal import convolve2d

# load the image
pic = imageio.imread('<image location>')
plt.figure(figsize = (6,6))
plt.imshow(pic);

# convolution function
def Convolution(image, kernel):
    conv_bucket = []
    for d in range(image.ndim):
        conv_channel = convolve2d(image[:,:,d], kernel,
                               mode="same", boundary="symm")
        conv_bucket.append(conv_channel)
    return np.stack(conv_bucket, axis=2).astype("uint8")

# different size of kernel
kernel_sizes = [9,15,30,60]
fig, axs = plt.subplots(nrows = 1, ncols = len(kernel_sizes), figsize=(15,15));

# iterate through all the kernel and convoluted image
for k, ax in zip(kernel_sizes, axs):
    kernel = np.ones((k,k))
    kernel /= np.sum(kernel)
    ax.imshow(Convolution(pic, kernel));
    ax.set_title("Convolved By Kernel: {}".format(k));
    ax.set_axis_off();
