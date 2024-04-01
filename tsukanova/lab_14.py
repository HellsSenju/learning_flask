import numpy as np


# количество слоёв - 3 + (23 % 3) = 5
# первый слой - 3 нейрона
# второй слой - 4 нейрона
# третий слой - 5 нейрона
# четвертый слой - 6 нейрона
# пятый(выходной) слой - 1 нейрон


# функция активации, np.exp(-x) - e в степени -х
def activation(x):
    return 1 / (1 + np.exp(-x))


# производная от функции активации
def sigma_derivative(x):
    return x * (1 - x)


# тренировочные образцы, строки - объекты, столбцы - признаки
# в данном случе три признака - на вход в нейронку придут x1, x2, x3
X = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0],
              [1, 1, 1]])

# матрица с откликами на каждый из образцов
y = np.array([[0],
              [1],
              [1],
              [0]])


np.random.seed(4)
# матрица весов между первым и вторым слоем
W_1_2 = 2 * np.random.random((3, 4)) - 1

# матрица весов между вторым и третьим слоем
W_2_3 = 2 * np.random.random((4, 5)) - 1

# матрица весов между третьим и четвертым слоем
W_3_4 = 2 * np.random.random((5, 6)) - 1

# матрица весов между четвертым и пятым слоем
W_4_5 = 2 * np.random.random((6, 1)) - 1

# скорость движения по антиградиенту
speed = 1.1
for j in range(100000):
    # l1, l2, l3, l4, l5 - матрицы определенного слоя сети
    l1 = X

    l2 = activation(np.dot(l1, W_1_2))
    l3 = activation(np.dot(l2, W_2_3))
    l4 = activation(np.dot(l3, W_3_4))
    l5 = activation(np.dot(l4, W_4_5))
    # ошибка на выходе (сразу для всех объектов) - ошибка пятого слоя
    l5_error = y - l5
    # модуль средней ошибки
    if (j % 10000) == 0:
        print("Error: " + str(np.mean(np.abs(l5_error))))

    # sigma - локальный градиент ошибки
    l5_sigma = l5_error * sigma_derivative(l5)

    l4_error = l5_sigma.dot(W_4_5.T)
    l4_sigma = l4_error * sigma_derivative(l4)

    l3_error = l4_sigma.dot(W_3_4.T)
    l3_sigma = l3_error * sigma_derivative(l3)

    l2_error = l3_sigma.dot(W_2_3.T)
    l2_sigma = l2_error * sigma_derivative(l2)

    # Обновляем веса
    W_4_5 += speed * l4.T.dot(l5_sigma)
    W_3_4 += speed * l3.T.dot(l4_sigma)
    W_2_3 += speed * l2.T.dot(l3_sigma)
    W_1_2 += speed * l1.T.dot(l2_sigma)

# Прямое распространение для тестовых данных
X_test = np.array([[0, 0, 0],
                   [0, 1, 1],
                   [1, 0, 1],
                   [1, 1, 0],
                   [0.5, 0.5, 0],
                   [0.5, 0.5, 1]])
# Y_test должен получиться [1, 0, 0, 1, 1, 0]
l1 = X_test
l2 = activation(np.dot(l1, W_1_2))
l3 = activation(np.dot(l2, W_2_3))
l4 = activation(np.dot(l3, W_3_4))
l5 = activation(np.dot(l4, W_4_5))
print(np.round(l5, 0))
