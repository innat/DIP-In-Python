""" Canny Edge Detection is based on the following five steps:

    1. Gaussian filter
    2. Gradient Intensity
    3. Non-maximum suppression
    4. Double threshold
    5. Edge tracking

    This module contains these five steps as five separate Python functions.
"""

# Third party imports
from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage import (sobel, generic_gradient_magnitude, generic_filter)
from scipy import ndimage
import numpy as np

# Module imports
from CannyEdge.utils import round_angle


def gs_filter(img, sigma):
    """ Step 1: Gaussian filter

    Args:
        img: Numpy ndarray of image
        sigma: Smoothing parameter

    Returns:
        Numpy ndarray of smoothed image
    """
    if type(img) != np.ndarray:
        raise TypeError('input image must be of type ndarray')
    else:
        return gaussian_filter(img, sigma)


def gradient_intensity(img):
    """ Step 2: Find gradients

    Args:
        img: Numpy ndarray of image to be processed (denoised image)

    Returns:
        grad: gradient-intensed image
        thetas: gradient directions
    """

    # Kernel for Gradient in x-direction
    sobel_x = np.array(
        [[-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]], np.int32
    )
    # Kernel for Gradient in y-direction
    sobel_y = np.array(
        [[1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]], np.int32
    )
    # Apply kernels to the image
    sx = ndimage.filters.convolve(img, sobel_x)
    sy = ndimage.filters.convolve(img, sobel_y)

    # return the hypothenuse of (Ix, Iy)
    grad = np.hypot(sx, sy) # Equivalent to sqrt(x1**2 + x2**2)
    thetas = np.arctan2(sy, sy) # Equivalent to tan inverse sy / sx

    return (grad, thetas)


def suppression(img, thetas):
    """ Step 3: Non-maximum suppression

    Args:
        img: Numpy ndarray of image to be processed (gradient-intensed image)
        D: Numpy ndarray of gradient directions for each pixel in img

    Returns:
        ...
    """
    # gray image shape
    h, w = img.shape
    z = np.zeros((h,w), dtype=np.int32)

    for i in range(h):
        for j in range(w):
            # find neighbour pixels to visit from the gradient directions
            loc = round_angle(thetas[i, j])
            try:
                if loc == 0:
                    if (img[i, j] >= img[i, j - 1]) and (img[i, j] >= img[i, j + 1]):
                        z[i,j] = img[i,j]
                elif loc == 90:
                    if (img[i, j] >= img[i - 1, j]) and (img[i, j] >= img[i + 1, j]):
                        z[i,j] = img[i,j]
                elif loc == 135:
                    if (img[i, j] >= img[i - 1, j - 1]) and (img[i, j] >= img[i + 1, j + 1]):
                        z[i,j] = img[i,j]
                elif loc == 45:
                    if (img[i, j] >= img[i - 1, j + 1]) and (img[i, j] >= img[i + 1, j - 1]):
                        z[i,j] = img[i,j]
            except IndexError as e:
                pass
    return z


def threshold(img, t, T):
    """ Step 4: Thresholding
    Iterates through image pixels and marks them as WEAK and STRONG edge
    pixels based on the threshold values.

    Args:
        img: Numpy ndarray of image to be processed (suppressed image)
        t: lower threshold
        T: upper threshold

    Return:
        img: Thresholdes image

    """
    # define gray value of a WEAK and a STRONG pixel
    cf = {
        'WEAK': np.int32(70),
        'STRONG': np.int32(255),
    }

    # get strong pixel indices
    strong_i, strong_j = np.where(img > T)

    # get weak pixel indices
    weak_i, weak_j = np.where((img >= t) & (img <= T))

    # get pixel indices set to be zero
    zero_i, zero_j = np.where(img < t)

    # set values
    img[strong_i, strong_j] = cf.get('STRONG')
    img[weak_i, weak_j] = cf.get('WEAK')
    img[zero_i, zero_j] = np.int32(0)

    return (img, cf.get('WEAK'))

def tracking(img, weak, strong=255):
    """ Step 5:
    Checks if edges marked as weak are connected to strong edges.

    Note that there are better methods (blob analysis) to do this,
    but they are more difficult to understand. This just checks neighbour
    edges.

    Also note that for perfomance reasons you wouldn't do this kind of tracking
    in a seperate loop, you would do it in the loop of the tresholding process.
    Since this is an **educational** implementation ment to generate plots
    to help people understand the major steps of the Canny Edge algorithm,
    we exceptionally don't care about perfomance here.

    Args:
        img: Numpy ndarray of image to be processed (thresholded image)
        weak: Value that was used to mark a weak edge in Step 4

    Returns:
        final Canny Edge image.
    """

    h, w = img.shape
    for i in range(h):
        for j in range(w):
            if img[i, j] == weak:
                # check if one of the neighbours is strong (=255 by default)
                try:
                    if ((img[i + 1, j] == strong) or (img[i - 1, j] == strong)
                         or (img[i, j + 1] == strong) or (img[i, j - 1] == strong)
                         or (img[i+1, j + 1] == strong) or (img[i-1, j - 1] == strong)):
                        img[i, j] = strong
                    else:
                        img[i, j] = 0
                except IndexError as e:
                    pass
    return img
