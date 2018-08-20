
# read details on blog post

import imageio
import numpy as np
import matplotlib.pyplot as plt

pic = imageio.imread('<image location>')
gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114])
gray = gray(pic)

max_ = np.max(gray)

'''
log transform
# s = c*log(1+r)
# r = np.log(1+gray)
# c = (L-1)/log(1+|I_max|)

'''
def log_transform():
    return 255/np.log(1+max_) * np.log(1+gray)

plt.figure(figsize = (5,5))
plt.imshow(log_transform()[:,300:1500], cmap = plt.get_cmap(name = 'gray'))
