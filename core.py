from engineModule import sharpen_all, evaluate_ed, evaluate_c, evaluate_hqi, find_winner
from histogram_equalization import HistogramEqualization
from openCV import OpenCVSharpen
from pillow import PillowSharpen
import glob

directory = 'C:\\Users\\kamil\\Desktop\\praca_dyplomowa\\archiwa_test\\'
index = 0
oc_full = 0
p_full = 0
he_full = 0

oc_test = 0
p_test = 0
he_test = 0

PATH = 'C:\\Users\\kamil\\Desktop\\praca_dyplomowa\\archiwa\\1.jpg'

pil = PillowSharpen(PATH)
op = OpenCVSharpen(PATH)
hist_eq = HistogramEqualization(PATH)


for filename in glob.glob(directory + '/*.jpg'):
    op.clear_object(filename)
    pil.clear_object(filename)
    hist_eq.clear_object(filename)
    os, ps, hs = sharpen_all(op, pil, hist_eq)
    ed = evaluate_ed(op, pil, hist_eq, os, ps, hs)
    c = evaluate_c(op, pil, hist_eq, os, ps, hs)
    hqi = evaluate_hqi(op, pil, hist_eq)

    if ed == 1:
        oc_test+=1
    if ed== 2:
        p_test +=1
    if ed == 3:
        he_test += 1

    if c == 1:
        oc_test+=1
    if c== 2:
        p_test +=1
    if c == 3:
        he_test += 1

    if hqi == 1:
        oc_test+=1
    if hqi == 2:
        p_test +=1
    if hqi == 3:
        he_test += 1

    val = find_winner(ed, c, hqi)
    if val == 1:
        oc_full+=1
    if val == 2:
        p_full +=1
    if val == 3:
        he_full += 1


    index += 1
print("total winner for 20 images")
print("openCV won: " + str(oc_full) + ", pillow: " + str(p_full) + " and histogram equalization: " + str(he_full))
print("winner for all test's")
print("openCV won: " + str(oc_test) + ", pillow: " + str(p_test) + " and histogram equalization: " + str(he_test))




