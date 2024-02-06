from models import products, B, G, Y, Kkal, Price
import models as models
from geneticAlgorithm import get_variant_properties, get_ration, fitness_function
from math import sqrt


def check(b, g, y, kkal, price) -> bool:
    if price > Price:
        return False
    if abs(b - B) > models.max_difference_b:
        return False
    if abs(g - G) > models.max_difference_g:
        return False
    if abs(y - Y) > models.max_difference_y:
        return False
    if abs(kkal - Kkal) > models.max_difference_k:
        return False

    return True


def full_search():
    stop = ''
    for _ in products:
        stop += "1"

    k = 0
    min_f = 1000000
    best_variant = []
    while True:
        binary = f'{k:07b}'
        if binary == stop:
            break

        b, g, y, kkal, price = 0, 0, 0, 0, 0
        variant = []
        for index, c in enumerate(binary):
            variant.append(int(c))
            if c == '1':
                b += products[index].b
                g += products[index].g
                y += products[index].y
                kkal += products[index].kkal
                price += products[index].price

        f = sqrt((b - B) ** 2 + (g - G) ** 2 + (y - Y) ** 2 + (kkal - Kkal) ** 2)
        if f < min_f and price <= Price:
            min_f = f
            best_variant = variant

        k += 1

    print("Результат полного перебора:")
    print(f'{get_ration(best_variant)}, f = {fitness_function(best_variant)}')
