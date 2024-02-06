from models import products, B, G, Y, Kkal
from random import choices
from geneticAlgorithm import genetic_algorithm, get_variant_properties, get_ration
from fullSearch import full_search


# функция приспособленности - корень из суммы квадратов

list = [ 5, 8, 2, 4, 14, 78, 3, 25, 8, 2, 35]

[x[0] for x in sorted(enumerate(list), key=lambda x: x[1])[:len()]]



# популяция - пространство гипотез
population = []

print("population", population)
print()
print(f"норма b, g, y, kkal - {B}, {G}, {Y}, {Kkal}")
print()


# for i in range(15):
#     population, f = genetic_algorithm(population)
#
# res = [x[0] for x in sorted(enumerate(f), key=lambda x: x[1])[:1]]
# print("genetic algorithm result", population[res[0]])
# print(get_ration(population[res[0]]))
# print("Итого по характеристикам - b, g, y, kkal - ", get_variant_properties(population[res[0]]))
#
# print()
#
# full_search_result, b, g, y, kkal = full_search()
# print("full search result: ", full_search_result)
# print(get_ration(full_search_result))
# print("Итого по характеристикам - b, g, y, kkal - ", b, g, y, kkal)


