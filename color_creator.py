import numpy as np
import time


class ColorCreationClass:
    def __init__(self, height_map):
        self.height_map = height_map

    def create_color_map(self):
        start = time.time()
        color = np.zeros((1024, 768, 3))
        average = np.mean(self.height_map)
        for i, val in enumerate(self.height_map):
            for j, val_j in enumerate(val):
                if np.mean(val_j) <= average:
                    color[i, j] = np.array([0, 255, 0])
                else:
                    color[i, j] = np.array([255, 255, 255])
        print(time.time() - start)
        return color


class ColorCreatorOptimization(ColorCreationClass):

    def create_color_map(self):
        start = time.time()
        color = np.empty((1024, 768, 3))
        color.fill(120)
        average = np.mean(self.height_map)
        color[self.height_map <= average] = (100, 255, 100)
        print(time.time() - start)
        return color


"""

(R, G, B) 
average ( 100, 255, 100 )
max( 255, 255, 222 )
min( 0, 255, 0 )
"""


class ColorCreatorMoreRealistic(ColorCreationClass):
    def create_color_map(self):
        color = np.empty((1024, 768, 3))
        max = np.amax(self.height_map)
        min = np.amin(self.height_map)

        return color


class ColorCreator:

    def __init__(self, height_map):
        self.color_creator = ColorCreatorOptimization(height_map)

    def create_color_map(self):
        return self.color_creator.create_color_map()
