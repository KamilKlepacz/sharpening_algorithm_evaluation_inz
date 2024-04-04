from engineModule import sharpen_all, evaluate_ed, evaluate_c, evaluate_hqi
from histogram_equalization import HistogramEqualization
from openCV import OpenCVSharpen
from pillow import PillowSharpen

pil = PillowSharpen()
op = OpenCVSharpen()
hist_eq = HistogramEqualization()
# pil.path = path
# op.path = path
# hist_eq.path = path

os, ps, hs = sharpen_all(op, pil, hist_eq)
evaluate_ed(op, pil, hist_eq, os, ps, hs)
evaluate_c(op, pil, hist_eq, os, ps, hs)
evaluate_hqi(op, pil, hist_eq)





