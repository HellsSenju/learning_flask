from random import uniform


class Clustering:
    def __init__(self, objects, k=3, m=1.6, e=0.0001, max_iter=30):
        self.objects = objects
        self.k = k
        self.m = m
        self.e = e
        self.max_iter = max_iter
        self.matrix = []
        self.clusters = []

    def fit(self):
        # заполнение матрицы степеней принадлежности
        for i in range(len(self.objects)):
            line = []
            to = 0.9
            for j in range(self.k - 1):
                line.append(uniform(0.1, to))
                to = to - line[len(line) - 1]

            line.append(1 - sum(line))
            if sum(line) != 1:
                line[1] += 1 - sum(line)
            self.matrix.append(line)

        func = 99999999
        iter_ = 0
        while True:
            # вычисление центров кластеров:
            self.clusters.clear()
            for j in range(self.k):
                numerator = 0  # числитель
                denominator = 0  # знаменатель

                for i in range(len(self.objects)):
                    numerator += (self.matrix[i][j] ** 1.6) * self.objects[i]
                    denominator += self.matrix[i][j] ** 1.6

                self.clusters.append(round(numerator / denominator, 6))

            # вычисление матрицы степеней принадлежности
            self.matrix.clear()
            for i in range(len(self.objects)):
                line = []
                for j in range(len(self.clusters)):
                    sum_ = 0
                    x_c = abs(self.objects[i] - self.clusters[j])
                    print(x_c)

                    if x_c == 0:
                        for k in range(len(self.clusters)):
                            if k == j:
                                line.append(1)
                            else:
                                line.append(0)

                    for l_ in range(len(self.clusters)):
                        sum_ += round((x_c / abs(self.objects[i] - self.clusters[l_]))**3.33, 6)

                    line.append(round(1 / sum_, 6))

                self.matrix.append(line)

            # вычисление значения целевой функции
            summ = 0
            for i in range(len(self.objects)):
                for j in range(len(self.clusters)):
                    summ += (self.matrix[i][j]**self.m) * abs(self.objects[i] - self.clusters[j])

            iter_ += 1
            if abs(summ - func) <= self.e or iter_ >= self.max_iter:
                return
            func = summ

    def print(self):
        print('print')
        cl = '            '
        for i in range(len(self.clusters)):
            cl += f'{round(self.clusters[i], 4)}          '

        print(cl)
        print('-------------------------------------------------------------------------------')
        for i in range(len(self.objects)):
            obj = f'{self.objects[i]} =         '
            for j in range(len(self.clusters)):
                obj += f'{self.matrix[i][j]}        '

            print(obj)



