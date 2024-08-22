import cv2
import numpy as np

from criteria_modules.UniqueColorModule import colors_difference
from criteria_modules.EdgeDetectionModule import edge_detection, edge_wideness, edge_difference
from criteria_modules.HistogramQualityIndexModule import count_quality_index
from helpers import blur_the_image


class OpenCVSharpen:
    def __init__(self, path):
        self.image = cv2.imread(path)
        self.ed_crit = None
        self.c_crit = None
        self.hqi_crit = None

    def show_image(self):
        cv2.imshow('test', self.image)
        cv2.waitKey()

    def sharpen_image(self):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        sharpened = cv2.filter2D(src=self.image, ddepth=-5, kernel=kernel)
        return sharpened

    def change_value_of_an_image(self, img):
        self.image = img

    def clear_object(self, path):
        self.image = cv2.imread(path)
        self.ed_crit = None
        self.c_crit = None
        self.hqi_crit = None

    def save_image(self, image):
        cv2.imwrite('sharpimage_oc.jpg', image)


    def criteria_ed(self, sharpened_img):
        edges_before = edge_detection(self.image)
        worked = False
        wpct_b, bpct_b, flag_b = edge_wideness(edges_before)
        edges_after = edge_detection(sharpened_img)
        wpct_a, bpct_a, flag_a = edge_wideness(edges_after)
        if flag_b and flag_a:
            total_diff, worked = edge_difference(wpct_b, wpct_a)
            self.ed_crit = total_diff
            if worked:
                print("Image got sharpened by OpenCV. Edge detection criteria detected "
                      + str(abs(total_diff)) + "% improvement from the original picture.")
                return total_diff
            else:
                print("value of sharpened image is " + str(abs(total_diff)) + "% wider than original which indicates it"
                                                                         " didn't sharpened")

        else:
            print("something went wrong in edge detection criteria for Pillow sharpened image")
            total_diff, worked = edge_difference(wpct_b, wpct_a)
            self.ed_crit = total_diff
            return total_diff

    def criteria_ch(self, sharpened_img):
        worked = False
        total_diff, worked = colors_difference(self.image, sharpened_img)
        self.c_crit = total_diff
        if worked:
            print("Image got sharpened by OpenCV. Unique color criteria detected "
                  + str(total_diff) + " more unique colours from the original picture.")
            return total_diff
        else:
            print("value of sharpened image is " + str(total_diff) + "less unique colours from the original picture"
                                                                     "which indicates it didn't got sharpened")

    def criteria_HQI(self):
        origin = self.image
        blured = blur_the_image(self.image)
        self.change_value_of_an_image(blured)
        sharpened = self.sharpen_image()
        index_of_quality = count_quality_index(origin, sharpened)
        print("Image got sharpened by OpenCV and got "
              + str(index_of_quality) + " score by index of quality based on histogram.")
        self.hqi_crit = index_of_quality
        return index_of_quality
