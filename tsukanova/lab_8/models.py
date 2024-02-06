from collections import namedtuple

# белки - b, жиры - g, углеводы - y
B = 70  # норма
G = 60  # норма
Y = 130  # норма
Kkal = 750  # норма
Price = 1700  # максимальная цена
max_difference = 20  # максимальная разница между нормой и текущем значением
max_difference_b = 5
max_difference_g = 10
max_difference_y = 20
max_difference_k = 50

Product = namedtuple('Product', ['name', 'b', 'g', 'y', 'kkal', 'price'])

products = [
    Product('Product 1', 25, 50, 30, 480, 245),
    Product('Product 2', 19, 13, 3, 190, 333),
    Product('Product 3', 22, 35, 65, 200, 530),
    Product('Product 4', 20, 1, 11, 90, 1300),
    Product('Product 5', 21, 13, 2, 105, 780),
    Product('Product 6', 21, 8, 50, 94, 900),
    Product('Product 7', 40, 12, 33, 309, 150),
    # Product('Product 8', 34, 8, 25, 50),
    # Product('Product 9', 30, 61, 11, 159),
    # Product('Product 10', 41, 33, 6, 120)
]