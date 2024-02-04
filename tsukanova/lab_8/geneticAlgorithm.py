from random import  randint
from math import sqrt
from lab8 import products, _b, _g, _y, _kkal


def crossover(_population: []) -> []:
    population_size = len(_population)
    for i in range(population_size):
        index_parent_1 = randint(0, population_size - 1)
        parent_1 = _population[index_parent_1]  # Родитель 1

        index_parent_2 = randint(0, population_size - 1)
        while index_parent_2 == index_parent_1:
            index_parent_2 = randint(0, population_size - 1)

        parent_2 = _population[index_parent_2]  # Родитель 2
        child = []

        div = int(len(products) / 2)
        for j in range(0, div):
            child.append(parent_1[j])

        for j in range(div, len(products)):
            child.append(parent_2[j])

        _population.append(child)

    return _population


def get_variant_properties(variant: []):
    b, g, y, kkal = 0, 0, 0, 0

    for i in range(len(variant)):
        if variant[i] == 1:
            b += products[i].b
            g += products[i].g
            y += products[i].y
            kkal += products[i].kkal

    return b, g, y, kkal


def selection(_population: []) -> []:
    f = []
    for variant in _population:
        b, g, y, kkal = get_variant_properties(variant)

        # квадраты разницы полученных значений с нормой
        b_difference = (b - _b) ** 2
        g_difference = (g - _g) ** 2
        y_difference = (y - _y) ** 2
        kkal_difference = (kkal - _kkal) ** 2

        f.append(sqrt(b_difference + g_difference + y_difference + kkal_difference))

    return [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:len(_population)]]


def genetic_algorithm(_population: []):
    # скрещивание
    population_after_crossover = crossover(_population)

    # отбор
    selected = selection(population_after_crossover)

    new_population = []
    for el in selected:
        new_population.append(population_after_crossover[el])

    return new_population, selected

