
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

if __name__ == '__main__':
    
    # load the image
    pic = imageio.imread('F:/demo_1.jpg')
    
    # seperate the row and column values
    total_row , total_col , layers = pic.shape
    
    '''
    Create vector.
    
    Ogrid is a compact method of creating a multidimensional-
    ndarray operations in single lines.
    for ex:
    
    >>> ogrid[0:5,0:5]
    output: [array([[0],
                    [1],
                    [2],
                    [3],
                    [4]]), 
            array([[0, 1, 2, 3, 4]])]
            
    '''
    x , y = np.ogrid[:total_row , :total_col]

    # get the center values of the image
    cen_x , cen_y = total_row/2 , total_col/2
    
    
    '''
    Measure distance value from center to each border pixel.
    To make it easy, we can think it's like, we draw a line from center-
    to each edge pixel value --> s**2 = (Y-y)**2 + (X-x)**2 
    '''
    distance_from_the_center = np.sqrt((x-cen_x)**2 + (y-cen_y)**2)

    # Select convenient radius value
    radius = (total_row/2)

    # Using logical operator '>' 
    '''
    logical operator to do this task which will return as a value 
    of True for all the index according to the given condition
    '''
    circular_pic = distance_from_the_center > radius

    '''
    let assign value zero for all pixel value that outside the cirular disc.
    All the pixel value outside the circular disc, will be black now.
    '''
    pic[circular_pic] = 0
    plt.figure(figsize = (10,10))
    plt.imshow(pic) 
    plt.show()