import numpy as np
from matplotlib import pyplot as plt


def histogram_creation(image):
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    plt.hist(image.flatten(), 256, [0, 256])
    plt.xlim([0, 256])
    # plt.show() #only if needed
    return hist


def count_quality_index(image, sharpen_image):
    # first we need to create histograms for both pictures
    original_hist = histogram_creation(image)
    sharpen_hist = histogram_creation(sharpen_image)

    # Now we resolve total change factor value
    diff = abs(sharpen_hist - original_hist)
    diff_sum = diff.sum()
    max_diff_factor = 2 * image.shape[0] * image.shape[1]
    total_ch_factor = 1 - (diff_sum / max_diff_factor)

    # Next step is to count Histogram Distortion value
    hist_multiplication = sharpen_hist * original_hist
    hist_sum_HD = hist_multiplication.sum()
    hist_exp = original_hist ** 2
    exp_sum_HD = hist_exp.sum()
    HD = hist_sum_HD / exp_sum_HD

    # Now we multiply tcValue and HD value
    index_of_quality = total_ch_factor * HD

    return index_of_quality
