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
