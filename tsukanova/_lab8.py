from collections import namedtuple
from random import choices, randint
from math import sqrt

# белки - b, жиры - g, углеводы - y
_b = 70  # норма
_g = 45  # норма
_y = 100  # норма
_kkal = 750  # норма

Product = namedtuple('Product', ['name', 'b', 'g', 'y', 'kkal'])

products = [
    Product('Свинина', 12, 50, 0, 480),
    Product('Говядина', 19, 13, 0, 190),
    Product('Баранина', 16, 15, 0, 200),
    Product('Телятина', 20, 1, 0, 90),
    Product('Кролик', 21, 13, 0, 197),
    Product('Курица', 21, 8, 0.8, 160),
    Product('Индейка', 22, 12, 0.6, 190),
    Product('Цыплята', 19, 8, 0.5, 160),
    Product('Утки', 16, 61, 0, 350),
    Product('Гуси', 16, 33, 0, 360)
]


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
    b = 0
    g = 0
    y = 0
    kkal = 0
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


# популяция - пространство гипотез
population = []
# заполнение популяции
for i in range(50):
    population.append(choices([0, 1], k=len(products)))

print("population", population)

# функция приспособленности - корень из суммы квадратов
f = []

for i in range(15):
    population, f = genetic_algorithm(population)

res = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]]
print("res", population[res[0]])
print("b, g, y, kkal", get_variant_properties(population[res[0]]))
print(f"норма b, g, y, kkal - {_b}, {_g}, {_y}, {_kkal}")



