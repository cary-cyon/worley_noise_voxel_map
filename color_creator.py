import numpy as np
import time
import ColorMap


class ColorCreationClass:
    def __init__(self, height_map, colormap=ColorMap.ColorMap(np.array([255, 0, 0]), np.array([0, 0, 255]))):
        self.height_map = height_map
        self.color_map = colormap


    def _map(self, value, start_old, end_old, start_new, end_new):

        return int(start_new + value * ((end_new-start_new)/(end_old-start_old)))

    def create_color_map(self):
        start = time.time()
        color = np.empty((1024, 768, 3))
        max_point = self.height_map.max()
        for i in range(self.height_map.shape[0]):
            for j in range(self.height_map.shape[1]):
                color[i, j] = self.color_map.get_color(
                                                    self._map(
                                                        self.height_map[i, j],
                                                        0,
                                                        255,
                                                        0,
                                                        max_point
                                                    ))

        print(time.time() - start)
        return color





