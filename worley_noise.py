import numpy as np
import time
from numba import njit
import matplotlib.pyplot as plt

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

        return start_new + value * ((end_new-start_new)/(end_old-start_old))

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


class WorleyNoiseSine(WorleyNoise):
    def get_worley_noise(self):

        start = time.time()
        distances = np.empty((self.field_width, self.field_height))
        distances = smaller_distance_calculate(distances,
                                               self.field_width,
                                               self.field_height,
                                               self.vertex)

        noise = self._map(distances, 0, distances.max(), 0, np.pi)
        print(time.time() - start)
        noise = np.sin(noise)*255
        print(time.time() - start)
        #np.full((1024, 768), 255) -
        return noise.astype('int32') -20

# test_gen1 = WorleyNoise(20,1024,768)
#
# plt.imshow(test_gen1.get_worley_noise())

# test_gen = WorleyNoiseSine(20, 1024, 768)
#
# plt.imshow(test_gen.get_worley_noise())
# plt.show()