import random
import numpy as np


class Clustering:
    def __init__(self, k=6):
        self.centroids = None
        self.k = k

    def fit(self, data):
        # выбираются центроиды
        self.centroids = [random.choice(data)]
        for i in range(self.k - 1):
            self.centroids += [random.choice(data)]

        clusters = [[] for i in range(self.k)]
        prev_centroids = None

        i = 0
        # нахождение новых центроидов
        while np.not_equal(self.centroids, prev_centroids).any():
            if i == 300:
                raise Exception("Превышено количество итераций")

            for item in data:
                # расстояния от точки до каждого центроида
                d = np.sqrt(np.sum((item - self.centroids)**2, axis=1))
                # заносим точку в нужный кластер
                clusters[np.argmin(d)].append(item)

            prev_centroids = self.centroids
            # новый центроид кластера - среднее значение принадлежащих ему точек
            self.centroids = [np.mean(cluster, axis=0) for cluster in clusters]

            # если у кластера нет точек, ему присваивается предыдущий центроид
            for i, centroid in enumerate(self.centroids):
                if np.isnan(centroid).any():
                    self.centroids[i] = prev_centroids[i]
            i += 1

    def predict(self, data):
        result = []

        for item in data:
            d = np.sqrt(np.sum((item - self.centroids) ** 2, axis=1))
            result.append(np.argmin(d))

        return result

