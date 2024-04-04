import skimage
import numpy as np
from skimage import img_as_ubyte


def blur_the_image(image):
    sigma = 3.0
    if not isinstance(image, np.ndarray):
        image = np.array(image)
    blurred = skimage.filters.gaussian(image, sigma=(sigma, sigma), truncate=4, channel_axis=-1)
    cv_image = img_as_ubyte(blurred)
    return cv_image
