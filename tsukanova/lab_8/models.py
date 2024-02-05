from collections import namedtuple

# белки - b, жиры - g, углеводы - y
_b = 70  # норма
_g = 60  # норма
_y = 130  # норма
_kkal = 750  # норма

Product = namedtuple('Product', ['name', 'b', 'g', 'y', 'kkal'])

products = [
    Product('Product 1', 25, 50, 30, 480),
    Product('Product 2', 19, 13, 3, 190),
    Product('Product 3', 22, 15, 65, 200),
    Product('Product 4', 20, 1, 11, 90),
    Product('Product 5', 21, 13, 2, 105),
    Product('Product 6', 21, 8, 50, 94),
    Product('Product 7', 40, 12, 33, 309),
    # Product('Product 8', 34, 8, 25, 50),
    # Product('Product 9', 30, 61, 11, 159),
    # Product('Product 10', 41, 33, 6, 120)
]