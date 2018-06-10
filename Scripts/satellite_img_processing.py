
"""
Image Data Analysis Using Numpy & OpenCV

author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('F:\satimg.jpg')
plt.figure(figsize = (10,10))
plt.imshow(pic)
plt.show()

print(f'Shape of the image {pic.shape}')
print(f'hieght {pic.shape[0]} pixels')
print(f'width {pic.shape[1]} pixels')

# Detecting High Pixel of Each Channel

# Only Red Pixel value , higher than 180
pic = imageio.imread('F:\satimg.jpg')
red_mask = pic[:, :, 0] < 180

pic[red_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)


# Only Green Pixel value , higher than 180
pic = imageio.imread('F:\satimg.jpg')
green_mask = pic[:, :, 1] < 180

pic[green_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)


# Only Blue Pixel value , higher than 180
pic = imageio.imread('F:\satimg.jpg')
blue_mask = pic[:, :, 2] < 180

pic[blue_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(pic)

# Composite mask using logical_and
pic = imageio.imread('F:\satimg.jpg')
final_mask = np.logical_and(red_mask, green_mask, blue_mask)
pic[final_mask] = 40
plt.figure(figsize=(15,15))
plt.imshow(pic)