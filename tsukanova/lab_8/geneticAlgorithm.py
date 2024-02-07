from random import randint, choices
from math import sqrt
from models import products, B, G, Y, Kkal
import models


def mutation_variant(variant: list[int]) -> list[int]:
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

    return variant


def crossover(_population: list) -> list:
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


def get_variant_properties(variant: list[int]):
    b, g, y, kkal, price = 0, 0, 0, 0, 0

    for i in range(len(variant)):
        if variant[i] == 1:
            b += products[i].b
            g += products[i].g
            y += products[i].y
            kkal += products[i].kkal
            price += products[i].price

    return b, g, y, kkal, price


def get_ration(variant: list[int]):
    res = 'Рацион: '
    for i in range(len(variant)):
        if variant[i] == 1:
            res += products[i].name + '  '

    return res


def fitness_function(variant: list[int]):
    b, g, y, kkal, price = get_variant_properties(variant)
    if price <= models.Price:
        return sqrt((b - B) ** 2 + (g - G) ** 2 + (y - Y) ** 2 + (kkal - Kkal) ** 2)
    else:
        return 10000000


def selection(_population: list):
    f = []
    for variant in _population:
        f.append(fitness_function(variant))

    new_population = []
    for el in [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:int(len(_population)/2)]]:
        new_population.append(_population[el])

    index_of_best = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]][0]
    return new_population, _population[index_of_best], f[index_of_best]


def mutation_population(_population: list) -> list:
    for i in range(len(_population)):
        _population[i] = mutation_variant(_population[i])

    return _population


def fill_population(population_size: int) -> list:
    return [choices([0, 1], k=len(products)) for _ in range(population_size)]
    # population = []
    # for i in range(population_size):
    #     population.append(choices([0, 1], k=len(products)))
    #
    # return population


def print_population(population: list, generation: int):
    print(f"=======Популяция, {generation} поколения=======")
    for i in range(len(population)):
        print(f'[{i + 1}] : {get_ration(population[i])}, f = {fitness_function(population[i])}')

    print("=================================================")


def genetic_algorithm(population_size: int, generations: int):
    population = fill_population(population_size)
    print_population(population, 0)
    f = 0
    best_variant = []
    # критерий остановки - кол-во шагов эволюции
    for _ in range(generations):
        # скрещивание
        population_after_crossover = crossover(population)

        # отбор (возвращает отобранную популяцию, лучший вариант из нее,
        # значение функции приспособленности этого варианта)
        population, best_variant, f = selection(population_after_crossover)

    print("Результат генетического алгоритма:")
    print(f'{get_ration(best_variant)}, f = {f}')

