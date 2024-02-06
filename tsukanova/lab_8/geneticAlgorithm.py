from random import randint, choices
from math import sqrt
from models import products, B, G, Y, Kkal


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

        # div = int(len(products) / 2)
        div = randint(1, len(products) - 1)
        for j in range(0, div):
            child.append(parent_1[j])

        for j in range(div, len(products)):
            child.append(parent_2[j])

        child = mutation_variant(child)

        _population.append(child)

    return _population


def mutation_variant(variant: []) -> []:
    k = randint(0, int(len(variant) / 3))
    indexes = []
    while k > 0:
        index = randint(0, len(variant) - 1)
        while indexes.__contains__(index):
            index = randint(0, len(variant) - 1)

        indexes.append(index)

        if variant[index] == 1:
            variant[index] = 0
        else:
            variant[index] = 1

        k -= 1


def get_variant_properties(variant: []) -> object:
    b, g, y, kkal, price = 0, 0, 0, 0, 0

    for i in range(len(variant)):
        if variant[i] == 1:
            b += products[i].b
            g += products[i].g
            y += products[i].y
            kkal += products[i].kkal
            price += products[i].price

    return b, g, y, kkal, price


def get_ration(variant: []):
    res = 'Рацион: '
    for i in range(len(variant)):
        if variant[i] == 1:
            res += products[i].name + '  '

    return res


def selection(_population: []) -> []:
    f = []
    for variant in _population:
        b, g, y, kkal, price = get_variant_properties(variant)
        f.append(sqrt((b - B) ** 2 + (g - G) ** 2 + (y - Y) ** 2 + (kkal - Kkal) ** 2))

    new_population = []
    for el in [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:len(_population/2)]]:
        new_population.append(_population[el])

    return new_population


def mutation_population(_population: []) -> []:
    for i in range(len(_population)):
        _population[i] = mutation_variant(_population[i])

    return _population


def fill_population(population_size: int) -> []:
    population = []
    for i in range(population_size):
        population.append(choices([0, 1], k=len(products)))

    return population


def genetic_algorithm(_population: [], population_size: int, generations: int):
    population = fill_population(population_size)

    # критерий остановки - кол-во шагов эволюции
    for _ in range(generations):
        population_after_crossover = crossover(population)
        population = selection(population_after_crossover)

    # скрещивание
    population_after_crossover = crossover(_population)

    # отбор (возвращает индексы отобранных вариантов)
    population_after_selection = selection(population_after_crossover)

