def sharpen_all(op, pil, he):
    # Sharpening image
    open_cv_sharpen = op.sharpen_image()
    pillow_sharpen = pil.sharpen_image()
    hist_eq_enchanced = he.hist_enchance()

    return open_cv_sharpen, pillow_sharpen, hist_eq_enchanced


def evaluate_ed(op, pil, hist, open_cv_sharpen, pillow_sharpen, hist_eq_enchanced):
    op.criteria_ed(open_cv_sharpen)
    pil.criteria_ed(pillow_sharpen)
    hist.criteria_ed(hist_eq_enchanced)
    # evaluate best algoritm
    if op.ed_crit < pil.ed_crit and op.ed_crit < hist.ed_crit:
        print("open cv was the best with score " + str(op.ed_crit))
    elif pil.ed_crit < op.ed_crit and pil.ed_crit < hist.ed_crit:
        print("pillow was the best with score " + str(pil.ed_crit))
    elif hist.ed_crit < pil.ed_crit and hist.ed_crit < pil.ed_crit:
        print("histogram equalization was the best with score " + str(hist.ed_crit))


def evaluate_c(op, pil, hist, open_cv_sharpen, pillow_sharpen, hist_eq_enchanced):
    op.criteria_ch(open_cv_sharpen)
    pil.criteria_ch(pillow_sharpen)
    hist.criteria_ch(hist_eq_enchanced)
    # evaluate best algoritm
    if op.c_crit > pil.c_crit and op.c_crit > hist.c_crit:
        print("open cv was the best with score " + str(op.c_crit))
    elif pil.c_crit > op.c_crit and pil.c_crit > hist.c_crit:
        print("pillow was the best with score " + str(pil.c_crit))
    elif hist.c_crit > pil.c_crit and hist.c_crit > pil.c_crit:
        print("histogram equalization was the best with score " + str(hist.c_crit))


def evaluate_hqi(op, pil, hist):
    op.criteria_HQI()
    pil.criteria_HQI()
    hist.criteria_HQI()
    # evaluate best algoritm
    if op.hqi_crit > pil.hqi_crit and op.hqi_crit > hist.hqi_crit:
        print("open cv was the best with score " + str(op.hqi_crit))
    elif pil.hqi_crit > op.hqi_crit and pil.hqi_crit > hist.hqi_crit:
        print("pillow was the best with score " + str(pil.hqi_crit))
    elif hist.hqi_crit > pil.hqi_crit and hist.hqi_crit > pil.hqi_crit:
        print("histogram equalization was the best with score " + str(hist.hqi_crit))
