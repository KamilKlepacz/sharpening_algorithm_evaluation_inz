# ---------------------------------------edge_detection-----------------------------------------------------------------
# Edge detection function which does basically same thing as its name shows
from itertools import chain

import cv2
import numpy


def edge_detection(testing_image):
    # Convert to graycsale
    img_gray = cv2.cvtColor(testing_image, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

    return edges


# edge wideness counts pct of white color which is considered as edge in this case
def edge_wideness(edge_detected_image):
    lista = [numpy.unique(edge_detected_image, return_counts=True)]
    flatten_list = list(chain.from_iterable(lista))
    val_of_black = 0
    val_of_white = 0
    flag_test = False  # Test if we have only black and white, if anything is not as it should we have False flag
    if len(flatten_list[0]) == 2:
        if flatten_list[0][0] == 0:
            val_of_black = flatten_list[1][0]
            if flatten_list[0][1] == 255:
                val_of_white = flatten_list[1][1]
        elif flatten_list[0][1] == 0:
            val_of_black = flatten_list[1][1]
            if flatten_list[0][0] == 255:
                val_of_white = flatten_list[1][0]
        flag_test = True

    fullsize = val_of_black + val_of_white
    whitepct = (val_of_white / fullsize) * 100
    blackpct = (val_of_black / fullsize) * 100
    return whitepct, blackpct, flag_test


# This function resolves the difference between before and after edge wideness
# total diff: this parameter returns difference
# expected diff: this parameter returns if wideness pct didn't grown which is expected in this case
def edge_difference(white_pct_before, white_pct_after):
    total_diff = white_pct_after - white_pct_before
    expected_diff = False
    if white_pct_after < white_pct_before:
        expected_diff = True
    return total_diff, expected_diff
