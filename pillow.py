import numpy
from PIL import Image
from PIL import ImageFilter

from criteria_modules.ColorHistogramModule import colors_difference
from criteria_modules.EdgeDetectionModule import edge_detection, edge_wideness, edge_difference
from criteria_modules.HistogramQualityIndexModule import count_quality_index
from helpers import blur_the_image


class PillowSharpen:
    path = 'C:\\Users\\kamil\\Desktop\\archiwum.jpg'
    imageObject = Image.open(path)
    imageObjnp = numpy.array(imageObject)
    ed_crit = None
    c_crit = None
    hqi_crit = None

    def show_image(self):
        self.imageObject.show()

    def change_value_of_an_image(self, image):
        self.imageObject = image

    def sharpen_image(self):
        sharpened = self.imageObject.filter(ImageFilter.SHARPEN)
        sharp_img = numpy.array(sharpened)
        return sharp_img

    def criteria_ed(self, sharpened_img):
        sharp_img = numpy.array(sharpened_img)
        edges_before = edge_detection(self.imageObjnp)
        worked = False
        wpct_b, bpct_b, flag_b = edge_wideness(edges_before)
        edges_after = edge_detection(sharp_img)
        wpct_a, bpct_a, flag_a = edge_wideness(edges_after)
        if flag_b == True and flag_a == True:
            total_diff, worked = edge_difference(wpct_b, wpct_a)
            self.ed_crit = total_diff
            if worked:
                print("Image got sharpened by Pillow. Edge detection criteria detected "
                      + str(abs(total_diff)) + "% improvement from the original picture.")
                return total_diff
            else:
                print("Image got sharpened by Pillow. Value of sharpened image is "
                      + str(abs(total_diff)) + "% wider than original which indicates it "
                                          "didn't sharpened")

        else:
            print("something went wrong in edge detection criteria for Pillow sharpened image")
            pass

    def criteria_ch(self, sharpened_img):
        worked = False
        sharp_img = numpy.array(sharpened_img)
        total_diff, worked = colors_difference(self.imageObjnp, sharp_img)
        self.c_crit = total_diff
        if worked:
            print("Image got sharpened by Pillow. Unique color criteria detected "
                  + str(total_diff) + " more unique colours from the original picture.")
            return total_diff
        else:
            print("Image got sharpened by Pillow. Value of sharpened image is "
                  + str(total_diff) + "less unique colours from the original "
                                      "picture which indicates it didn't got sharpened")

    def criteria_HQI(self):
        origin = self.imageObject
        blured = blur_the_image(self.imageObject)
        self.change_value_of_an_image(Image.fromarray(blured))
        sharpened = self.sharpen_image()
        index_of_quality = count_quality_index(origin, sharpened)
        print("Image got sharpened by Pillow and got "
              + str(index_of_quality) + " score by index of quality based on histogram.")
        self.hqi_crit = index_of_quality
        return index_of_quality

