def sharpen_all(op, pil, he):
    # Sharpening image
    open_cv_sharpen = op.sharpen_image()
    pillow_sharpen = pil.sharpen_image()
    hist_eq_enchanced = he.hist_enchance()

    return open_cv_sharpen, pillow_sharpen, hist_eq_enchanced

def find_winner(a, b, c):
    w1 = 0
    w2 = 0
    w3 = 0

    if a == 0:
        pass
    elif a == 1:
        w1+=1
    elif a == 2:
        w2+=1
    elif a == 3:
        w3 += 1

    if b == 0:
        pass
    elif b == 1:
        w1+=1
    elif b == 2:
        w2+=1
    elif b == 3:
        w3 += 1

    if c == 0:
        pass
    elif c == 1:
        w1+=1
    elif c == 2:
        w2+=1
    elif c == 3:
        w3 += 1

    if w1 > w2 and w1 > w3:
        print("open cv won.")
        return 1
    elif w2 > w1 and w2 > w3:
        print("pillow won.")
        return 2
    elif w3 > w2 and w3 > w1:
        print("histogram equalization won")
        return 3
    else:
        return 0


#Winner is a variable that determines which algorithm was the best
# 0 - None
# 1 - open cv
# 2 - pillow
# 3 - histogram equalization
def evaluate_ed(op, pil, hist, open_cv_sharpen, pillow_sharpen, hist_eq_enchanced):
    op.criteria_ed(open_cv_sharpen)
    pil.criteria_ed(pillow_sharpen)
    hist.criteria_ed(hist_eq_enchanced)
    winner = 0
    # evaluate best algoritm
    if op.ed_crit < pil.ed_crit and op.ed_crit < hist.ed_crit:
        print("open cv was the best with score " + str(op.ed_crit))
        winner = 1
    elif pil.ed_crit < op.ed_crit and pil.ed_crit < hist.ed_crit:
        print("pillow was the best with score " + str(pil.ed_crit))
        winner = 2
    elif hist.ed_crit < pil.ed_crit and hist.ed_crit < pil.ed_crit:
        print("histogram equalization was the best with score " + str(hist.ed_crit))
        winner = 3
    return winner


def evaluate_c(op, pil, hist, open_cv_sharpen, pillow_sharpen, hist_eq_enchanced):
    op.criteria_ch(open_cv_sharpen)
    pil.criteria_ch(pillow_sharpen)
    hist.criteria_ch(hist_eq_enchanced)
    winner = 0
    # evaluate best algoritm
    if op.c_crit > pil.c_crit and op.c_crit > hist.c_crit:
        print("open cv was the best with score " + str(op.c_crit))
        winner = 1
    elif pil.c_crit > op.c_crit and pil.c_crit > hist.c_crit:
        print("pillow was the best with score " + str(pil.c_crit))
        winner = 2
    elif hist.c_crit > pil.c_crit and hist.c_crit > pil.c_crit:
        print("histogram equalization was the best with score " + str(hist.c_crit))
        winner = 3
    return winner


def evaluate_hqi(op, pil, hist):
    op.criteria_HQI()
    pil.criteria_HQI()
    hist.criteria_HQI()
    winner = 0
    # evaluate best algoritm
    if op.hqi_crit > pil.hqi_crit and op.hqi_crit > hist.hqi_crit:
        print("open cv was the best with score " + str(op.hqi_crit))
        winner = 1
    elif pil.hqi_crit > op.hqi_crit and pil.hqi_crit > hist.hqi_crit:
        print("pillow was the best with score " + str(pil.hqi_crit))
        winner = 2
    elif hist.hqi_crit > pil.hqi_crit and hist.hqi_crit > pil.hqi_crit:
        print("histogram equalization was the best with score " + str(hist.hqi_crit))
        winner = 3

    return winner
