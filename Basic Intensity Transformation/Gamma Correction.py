
"""
Image Data Analysis Using Numpy & OpenCV
author: Mohammed Innat
email:  innat1994@gmail.com
website: https://iphton.github.io/iphton.github.io/
Please feel free to use and modify this, but keep the above information. Thanks!
"""


# read details on blog post

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
gamma = 2.2
original = ((pic/255) ** (1/gamma))

plt.imshow(original)
