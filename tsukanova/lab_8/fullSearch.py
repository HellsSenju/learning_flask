from models import products, _b, _g, _y, _kkal
from geneticAlgorithm import get_variant_properties
from math import sqrt


def full_search():
    stop = ''
    for el in products:
        stop += "1"

    k = 0
    min_f = 1000000
    best_variant = []
    while True:
        binary = f'{k:07b}'
        if binary == stop:
            break

        b, g, y, kkal = 0, 0, 0, 0
        variant = []
        for index, c in enumerate(binary):
            variant.append(int(c))
            if c == '1':
                b += products[index].b
                g += products[index].g
                y += products[index].y
                kkal += products[index].kkal

        f = abs(b - _b) + abs(g - _g) + abs(y - _y) + abs(kkal - _kkal)
        if f < min_f:
            min_f = f
            best_variant = variant

        k += 1
    b, g, y, kkal = get_variant_properties(best_variant)
    return best_variant, b, g, y, kkal