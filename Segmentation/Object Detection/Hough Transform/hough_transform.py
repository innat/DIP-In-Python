import imageio
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


def hough_line(img, angle_step = 1, white_lines = True, threshold = 5):

    """
    param:: img - 2D binary image
    param:: angle_step - Spacing between angles to use every n-th angle, Default step is 1.
    param:: lines_are_white - boolean indicator
    param:: value_threshold - Pixel values above or below the threshold are edges

    Returns:
    param:: accumulator - 2D array of the hough transform accumulator
    param:: theta - array of angles used in computation, in radians.
    param:: rhos - array of rho values.
    """
    # Rho and Theta ranges
    thetas = np.deg2rad(np.arange(-90.0, 90.0, angle_step))
    width, height = img.shape
    diag_len = int(np.ceil(np.sqrt(width * width + height * height)))
    rhos = np.linspace(-diag_len, diag_len, diag_len * 2)

    # Cache some resuable values
    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)

    # Hough accumulator array of theta vs rho
    accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint8)
    # (row, col) indexes to edges
    are_edges = img > threshold if white_lines else img < threshold
    y_idxs, x_idxs = np.nonzero(are_edges)

    # Vote in the hough accumulator
    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]

        for t_idx in range(num_thetas):
            # Calculate rho. diag_len is added for a positive index
            rho = diag_len + int(round(x * cos_t[t_idx] + y * sin_t[t_idx]))
            accumulator[rho, t_idx] += 1

    return accumulator, thetas, rhos


def viz_hough_line(img, accumulator, thetas, rhos, save_path=None):

    # plot
    fig, ax = plt.subplots(1, 2, figsize=(10, 10))

    ax[0].imshow(img, cmap=plt.cm.gray)
    ax[0].set_title('Input Image')
    ax[0].axis('image')

    ax[1].imshow( accumulator, cmap='jet', extent=[np.rad2deg(thetas[-1]),
                                                   np.rad2deg(thetas[0]), rhos[-1], rhos[0]])
    ax[1].set_aspect('equal', adjustable='box')
    ax[1].set_title('Hough Transform')
    ax[1].set_xlabel('Angles (deg)')
    ax[1].set_ylabel('Distance (px)')
    ax[1].axis('image')

    plt.axis('off')
    plt.show()


gray = lambda rgb : np.dot(rgb[... , :3] , [0.299 , 0.587, 0.114])

if __name__ == '__main__':
    # import and function calling
    pic = imageio.imread('<image location>')
    gray = gray(pic)

    accumulator, thetas, rhos = hough_line(gray) # get the parameter
    viz_hough_line(gray, accumulator, thetas, rhos) # visualization
