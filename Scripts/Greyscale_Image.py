
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

pic = imageio.imread('F:/demo_2.jpg')

gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114]) 
gray = gray(pic)  

plt.figure( figsize = (10,10))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.show()

'''
However, the GIMP converting color to grayscale image software 
has three algorithms to do the task.

Lightness The graylevel will be calculated as

Lightness = ½ × (max(R,G,B) + min(R,G,B))

Luminosity The graylevel will be calculated as

Luminosity = 0.21 × R + 0.72 × G + 0.07 × B

Average The graylevel will be calculated as

Average Brightness = (R + G + B) ÷ 3

'''

pic = imageio.imread('F:/demo_2.jpg')

gray = lambda rgb : np.dot(rgb[... , :3] , [0.21 , 0.72, 0.07]) 
gray = gray(pic)  

plt.figure( figsize = (10,10))
plt.imshow(gray, cmap = plt.get_cmap(name = 'gray'))
plt.show()

'''
Let's take a quick overview some the changed properties now the color image.
Like we observe some properties of color image, same statements are applying 
now for gray scaled image.
'''

print('Type of the image : ' , type(gray))
print()
print('Shape of the image : {}'.format(gray.shape))
print('Image Hight {}'.format(gray.shape[0]))
print('Image Width {}'.format(gray.shape[1]))
print('Dimension of Image {}'.format(gray.ndim))
print()
print('Image size {}'.format(gray.size))
print('Maximum RGB value in this image {}'.format(gray.max()))
print('Minimum RGB value in this image {}'.format(gray.min()))
print('Random indexes [X,Y] : {}'.format(gray[100, 50]))
