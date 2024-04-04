import cv2
import numpy


def hist_enchance(self):
    img = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
    clahe = cv2.createCLAHE(clipLimit=2)
    img[:, :, 0] = clahe.apply(img[:, :, 0]) + 30
    sharpened = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    return sharpened

# image = cv2.imread('C:\\Users\\kamil\\Desktop\\archiwumPRZED.jpg')
#
# image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
#
# # equalize the histogram of the Y channel
# image[:, :, 0] = cv2.equalizeHist(image[:, :, 0])
#
# # convert the YUV image back to RGB format
# img_output = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
#
# cv2.imshow('Histogram equalized', img_output)
# cv2.imwrite('C:\\Users\\kamil\\Desktop\\praca_dyplomowa\\obrazy_do_pracy\\rgbHistEQ_badQuality2.png', img_output)
#
# cv2.waitKey(0)

pic = cv2.imread('C:\\Users\\kamil\\Desktop\\archiwumPRZED.jpg')
r, g, b = cv2.split(pic)
kernel = numpy.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])
rs = cv2.filter2D(src=r, ddepth=-5, kernel=kernel)
gs = cv2.filter2D(src=g, ddepth=-5, kernel=kernel)
bs = cv2.filter2D(src=b, ddepth=-5, kernel=kernel)
newpic = cv2.filter2D(src=pic, ddepth=-5, kernel=kernel)
picture = cv2.merge((rs, gs, bs))
cv2.imshow('Histogram equalized', pic)
cv2.waitKey(0)
cv2.imshow('Histogram equalized', picture)
cv2.waitKey(0)
cv2.imshow('Histogram equalized', newpic)
cv2.waitKey(0)
cv2.imwrite('C:\\Users\\kamil\\Desktop\\przed_wyostrzaniem.jpg', pic)
cv2.imwrite('C:\\Users\\kamil\\Desktop\\r.jpg', r)
cv2.imwrite('C:\\Users\\kamil\\Desktop\\g.jpg', g)
cv2.imwrite('C:\\Users\\kamil\\Desktop\\b.jpg', b)
cv2.imwrite('C:\\Users\\kamil\\Desktop\\wyostrzone.jpg', picture)

