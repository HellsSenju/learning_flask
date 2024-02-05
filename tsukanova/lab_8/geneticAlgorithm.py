from random import randint, choices
from math import sqrt
from models import products, _b, _g, _y, _kkal


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


def get_ration(variant: []):
    res = 'Рацион: '
    for i in range(len(variant)):
        if variant[i] == 1:
            res += products[i].name + '  '

    return res


def selection(_population: []) -> []:
    f = []
    for variant in _population:
        b, g, y, kkal = get_variant_properties(variant)
        f.append(abs(b - _b) + abs(g - _g) + abs(y - _y) + abs(kkal - _kkal))

    return [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:len(_population)]]


def mutation(_population: []) -> []:
    for variant in _population:
        k = randint(0, int(len(variant)/3))
        indexes = []
        while k >= 0:
            index = randint(0, len(variant) - 1)
            while indexes.__contains__(index):
                index = randint(0, len(variant) - 1)

            indexes.append(index)

            if variant[index] == 1:
                variant[index] = 0
            else:
                variant[index] = 1

            k -= 1

    return _population


def genetic_algorithm(_population: []):
    # скрещивание
    population_after_crossover = crossover(_population)

    population_after_mutation = mutation(population_after_crossover)

    # отбор (возвращает индексы отобранных вариантов)
    selected = selection(population_after_mutation)

    new_population = []
    for el in selected:
        new_population.append(population_after_mutation[el])

    return new_population, selected

