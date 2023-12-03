import random
import numpy as np


class Clustering:
    def __init__(self, k=6):
        self.centroids = None
        self.k = k

    def do(self, data):
        # выбираются центроиды
        self.centroids = [random.choice(data)]
        for i in range(self.k - 1):
            self.centroids += [random.choice(data)]

        print(self.centroids)
        clusters = [[] for i in range(self.k)]
        prev_centroids = None
        while np.not_equal(self.centroids, prev_centroids).any():
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

    def adds(self, data):
        centroids = []
        centroid_id = []

        for item in data:
            d = np.sqrt(np.sum((item - self.centroids) ** 2, axis=1))
            centroid_id = np.argmin(d)
            centroids.append(self.centroids[centroid_id])
            centroid_id.append(centroid_id)

        return centroids, centroid_id

