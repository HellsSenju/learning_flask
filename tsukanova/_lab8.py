from collections import namedtuple
from random import choices, random

# белки - b, жиры - g, углеводы - y
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
    Product('Гуси', 16, 33, 0, 360),
]

# особь
variant = []
# популяция - пространство гипотез
population = []


# заполнение популяции
for i in range(3):
    population.append(choices([0, 1], k=10))



