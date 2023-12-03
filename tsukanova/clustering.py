import random
from array import array
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
        for item in data:
            # расстояния от точки до каждого центроида
            d = np.sqrt(np.sum((item - self.centroids)**2, axis=1))
            # заносим точку в нужный кластер
            clusters[np.argmin(d)].append(item)

        prev_centroids = self.centroids
        self.centroids = [np.mean(cluster, axis=0) for cluster in clusters]

        # если у кластера нет точек, ему присваивается предыдущий центроид
        for i, centroid in enumerate(self.centroids):
            if np.isnan(centroid).any():
                self.centroids[i] = prev_centroids[i]

