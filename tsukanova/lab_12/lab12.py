# индекс массы тела
imt = {
    'дефицит': [0, 0, 16, 19],
    'норма': [17, 22, 26],
    'избыток': [24, 28, 31],
    'ожирение': [29, 32, 50, 50]
}

# уровень глюкозы
glucose = {
    'мало': [0, 0, 3.2, 3.5],
    'норма': [3.1, 4.2, 5.7],
    'много': [5.3, 5.5, 10, 10]
}

# вероятность диабета
diabetes_probability = {
    'малая': [0, 0, 10, 40],
    'средняя': [30, 55, 80],
    'большая': [75, 100, 100, 100]
}

rules = [
    ['дефицит', 'мало', 'малая'],
    ['дефицит', 'норма', 'малая'],
    ['дефицит', 'много', 'средняя'],
    ['норма', 'мало', 'малая'],
    ['норма', 'норма', 'малая'],
    ['норма', 'много', 'средняя'],
    ['избыток', 'мало', 'средняя'],
    ['избыток', 'норма', 'средняя'],
    ['избыток', 'много', 'большая'],
    ['ожирение', 'мало', 'средняя'],
    ['ожирение', 'норма', 'большая'],
    ['ожирение', 'много', 'большая']
]


def triangular(params, value):
    a = params[0]
    b = params[1]
    c = params[2]

    if a <= value <= b:
        return round((value - a) / (b - a), 3)

    elif b < value <= c:
        return round((c - value) / (c - b), 3)

    elif value < a or value > c:
        return 0


def trapezoid(params, value):
    a = params[0]
    b = params[1]
    c = params[2]
    d = params[3]

    if a <= value <= b:
        return round((value - a) / (b - a), 3)

    elif b < value < c:
        return 1

    elif c <= value <= d:
        return round((d - value) / (d - c), 3)

    elif value < a or value > d:
        return 0


def defuz_trapezoid(params: []):
    return (params[1] + params[2]) / 2


input_imt = float(input("Введите индекс массы тела [0, 50]: "))
input_glucose = float(input("Введите уровень глюкозы [0, 10]: "))

# результаты импликации по всем правилам
res_impl = []
for item in rules:
    # степень принадлежности для значения "индекс массы тела"
    first = triangular(imt.get(item[0]), input_imt) if len(imt.get(item[0])) == 3 \
        else trapezoid(imt.get(item[0]), input_imt)

    # степень принадлежности для значения "уровень глюкозы"
    second = triangular(glucose.get(item[1]), input_glucose) if len(glucose.get(item[1])) == 3 \
        else trapezoid(glucose.get(item[1]), input_glucose)

    # нечеткое И (минимальное) = имитация моделируется через минимум
    res_impl.append(min(first, second))

# результат агрегации (максимальное)
agr = max(res_impl)
# полученное нечеткое значение вероятности диабета
res_str = rules[res_impl.index(agr)][2]
print(res_str)
# полученное четкое значение вероятности диабета
res = diabetes_probability.get(res_str)[1] if len(diabetes_probability.get(res_str)) == 3 \
    else defuz_trapezoid(diabetes_probability.get(res_str))

print(f'Вероятность диабета {res} %')
