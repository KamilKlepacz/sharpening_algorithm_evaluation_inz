import cv2
import numpy
import numpy as np

from criteria_modules.UniqueColorModule import colors_difference
from criteria_modules.EdgeDetectionModule import edge_detection, edge_wideness, edge_difference
from criteria_modules.HistogramQualityIndexModule import count_quality_index
from helpers import blur_the_image


class HistogramEqualization:
    def __init__(self, path):
        self.image = cv2.imread(path)
        self.ed_crit = None
        self.c_crit = None
        self.hqi_crit = None

    def hist_enchance(self):
        img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        clahe = cv2.createCLAHE(clipLimit=2)
        img[:, :, 0] = clahe.apply(img[:, :, 0]) + 30
        sharpened = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
        return sharpened

    def change_value_of_an_image(self, img):
        self.image = img

    def save_image(self, image):
        cv2.imwrite('sharpimage_he.jpg', image)

    def clear_object(self, path):
        self.image = cv2.imread(path)
        self.ed_crit = None
        self.c_crit = None
        self.hqi_crit = None

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
                print("Image got enchanced by histogram equalization. Edge detection criteria detected "
                      + str(abs(total_diff)) + "% improvement from the original picture.")
                return total_diff
            else:
                print("Image got enchanced by histogram equalization. Value of sharpened image is "
                      +  str(abs(total_diff)) + "% wider than original which indicates it "
                                          "didn't sharpened")
                return total_diff

        else:
            print("something went wrong in edge detection criteria for histogram equalization")
            total_diff, worked = edge_difference(wpct_b, wpct_a)
            self.ed_crit = total_diff
            return total_diff

    def criteria_ch(self, sharpened_img):
        worked = False
        total_diff, worked = colors_difference(self.image, sharpened_img)
        self.c_crit = total_diff
        if worked:
            print("Image got enchanced by histogram equalization. Unique color criteria detected "
                  + str(total_diff) + " more unique colours from the original picture.")
            return total_diff
        else:
            print("value of sharpened image is " + str(total_diff) + "less unique colours from the original picture"
                                                                     "which indicates it didn't got sharpened")

    def criteria_HQI(self):
        origin = self.image
        blured = blur_the_image(self.image)
        self.change_value_of_an_image(blured)
        sharpened = self.hist_enchance()
        index_of_quality = count_quality_index(origin, sharpened)
        print("Image got enchanced by histogram equalization and got "
              + str(index_of_quality) + " score by index of quality based on histogram.")
        self.hqi_crit = index_of_quality
        return index_of_quality
