
# read details on blog post

import imageio
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
plt.figure(figsize = (6,6))
plt.imshow(255 - pic);
