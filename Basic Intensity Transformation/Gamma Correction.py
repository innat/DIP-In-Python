
# read details on blog post

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
gamma = 2.2
original = ((pic/255) ** (1/gamma))

plt.imshow(original)
