from collections import namedtuple
from random import choices
from geneticAlgorithm import genetic_algorithm, get_variant_properties

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






# популяция - пространство гипотез
population = []

# заполнение популяции
for i in range(50):
    population.append(choices([0, 1], k=len(products)))

print("population", population)

# функция приспособленности - корень из суммы квадратов
f = []

# f'{6:010b}'


def full_search(_population):
    stop = ''
    for el in products:
        stop += "1"

    k = 0,
    while True:
        binary = f'{k:010b}'
        if binary == stop:
            return

        b, g, y, kkal = 0, 0, 0, 0
        for index, c in enumerate(binary):
            if c == '1':
                b += products[index].b
                g += products[index].g
                y += products[index].y
                kkal += products[index].kkal







for i in range(15):
    population, f = genetic_algorithm(population)

res = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]]
print("res", population[res[0]])
print("b, g, y, kkal", get_variant_properties(population[res[0]]))
print(f"норма b, g, y, kkal - {_b}, {_g}, {_y}, {_kkal}")



