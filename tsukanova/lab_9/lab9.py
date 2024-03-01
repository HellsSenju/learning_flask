from Model import Model

# универсальное множество
universal_set = [149, 150, 156, 158, 160, 163, 165, 166, 167, 169,
                 171, 172, 174, 175, 177,  180, 182, 185,  190, 191]

# параметры функций принадлежности
fuzzy_sets = [Model('Средний рост', 150, 160, 175),
              Model('Выше среднего', 165, 177, 185)]

# заполнение нечетких множеств
for x in universal_set:
    for fuzzy_set in fuzzy_sets:
        a = fuzzy_set.a
        b = fuzzy_set.b
        c = fuzzy_set.c

        if a <= x <= b:
            fuzzy_set.set[x] = round((x - a) / (b - a), 1)

        elif b < x <= c:
            fuzzy_set.set[x] = round((c - x) / (c - b), 1)

        elif x < a or x > c:
            fuzzy_set.set[x] = 0


average = fuzzy_sets[0].set
above_average = fuzzy_sets[1].set
print(average)
print(above_average)
result = []
# пересечение нечетких множеств (И - мин степень принадлежности)
for x in universal_set:
    result.append(min(average[x], above_average[x]))

print('Результат - пересечение')
print(result)







