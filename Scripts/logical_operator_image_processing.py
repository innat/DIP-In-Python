
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

pic = imageio.imread('F:/demo_1.jpg')
plt.figure(figsize = (10,10))
plt.imshow(pic)
plt.show()


low_pixel = pic < 20

# to ensure of it let's check if all values in low_pixel are True or not
if low_pixel.any() == True:
    print(low_pixel.shape)


print(pic.shape)
print(low_pixel.shape)  

'''
We generated that low value filter using a global  comparison operator for 
all the values less than 200. However, we can use this low_pixel array as an index 
to set those low values to some specific values which  may be higher than or lower 
than the previous pixel value.
'''

# randomly choose a value 
import random

# load the orginal image
pic = imageio.imread('F:/demo_1.jpg')

# set value randomly range from 25 to 225 - these value also randomly choosen
pic[low_pixel] = random.randint(25,225)

# display the image
plt.figure( figsize = (10,10))
plt.imshow(pic)
plt.show()