import numpy as np
import time
from numba import njit


@njit(fastmath=True)
def get_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))


@njit(fastmath=True)
def smaller_distance_calculate(distances, field_width, field_height, vertex):
    for i in range(field_width):
        for j in range(field_height):
            dist = field_height
            for ver in vertex:
                d = get_distance(np.array([i, j]), ver)
                if dist > d:
                    dist = d
            distances[i, j] = dist
    return distances


class WorleyNoise:

    def __init__(self, col_of_vertex, width, height):

        self.col_of_vertex = col_of_vertex
        self.field_width = width
        self.field_height = height
        self.vertex = np.random.random((col_of_vertex, 2))
        self.vertex[:, 0] = self.vertex[:, 0] * width
        self.vertex[:, 1] = self.vertex[:, 1] * height
        self.vertex = self.vertex.astype(int)

    def _map(self, value, start_old, end_old, start_new, end_new):

        return value * ((end_new-start_new)/(end_old-start_old))

    def get_worley_noise(self):

        start = time.time()
        distances = np.empty((self.field_width, self.field_height))
        distances = smaller_distance_calculate(distances,
                                               self.field_width,
                                               self.field_height,
                                               self.vertex)

        noise = self._map(distances, 0, self.field_height/2, 0, 255)

        print(time.time() - start)
        return noise.astype('int32')