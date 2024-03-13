import numpy


# -----------------------------------------color_criteria_module--------------------------------------------------------------
def nr_of_colors(image):
    lista = [numpy.unique(image.reshape(-1, image.shape[2]), axis=0)]
    counter = len(lista[0])
    return lista, counter

def colors_difference(image_b, image_a):
    list_a, count_a = nr_of_colors(image_a)
    list_b, count_b = nr_of_colors(image_b)

    total_diff = count_a - count_b
    expected_diff = False
    if (count_a - count_b) > 0:
        expected_diff = True
    return total_diff, expected_diff

#not needed anymore
def average_colors(list_in):
    black_count = 0
    white_count = 0
    blue_count = 0
    red_count = 0
    for x in list_in:
        if x[0] < 50 and x[1] < 50 and x[2] < 50:
            black_count = black_count + 1

    for x in list_in:
        if x[0] > 150 and x[1] > 150 and x[2] > 150:
            white_count = white_count + 1

    for x in list_in:
        if x[0] < 50 and x[1] < 50 and x[2] > 200:
            blue_count = blue_count + 1

    for x in list_in:
        if x[0] < 50 and x[1] < 50 and x[2] > 200:
            red_count = red_count + 1

    return black_count, white_count, blue_count, red_count


def color_histogram(color_list, picture):
    hashed_image = []
    histogram = []
    for a in picture:
        hashed_image.append(a[0] * 1000000 + a[1] * 1000 + a[2])
    for a in color_list:
        val = a[0] * 1000000 + a[1] * 1000 + a[2]
        temp = 0
        for b in hashed_image:
            if val == b:
                temp = temp + 1
        histogram.append(temp)
    return histogram
