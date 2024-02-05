from models import products, _b, _g, _y, _kkal
from random import choices
from geneticAlgorithm import genetic_algorithm, get_variant_properties, get_ration
from fullSearch import full_search


# популяция - пространство гипотез
population = []

# заполнение популяции
for i in range(25):
    population.append(choices([0, 1], k=len(products)))

print("population", population)
print()
print(f"норма b, g, y, kkal - {_b}, {_g}, {_y}, {_kkal}")
print()
# функция приспособленности - корень из суммы квадратов
f = []


for i in range(15):
    population, f = genetic_algorithm(population)

res = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]]
print("genetic algorithm result", population[res[0]])
print(get_ration(population[res[0]]))
print("Итого по характеристикам - b, g, y, kkal - ", get_variant_properties(population[res[0]]))

print()

full_search_result, b, g, y, kkal = full_search()
print("full search result: ", full_search_result)
print(get_ration(full_search_result))
print("Итого по характеристикам - b, g, y, kkal - ", b, g, y, kkal)


