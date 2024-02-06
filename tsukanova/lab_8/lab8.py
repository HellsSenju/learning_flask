from models import B, G, Y, Kkal
from geneticAlgorithm import genetic_algorithm
from fullSearch import full_search

# популяция - пространство гипотез

print()
print(f"норма b, g, y, kkal - {B}, {G}, {Y}, {Kkal}")
print()

genetic_algorithm(8, 100)

print()

full_search()


