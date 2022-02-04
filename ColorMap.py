import numpy as np

class ColorMap:

    def __init__(self, color1, color2):
        self.colormap = self.create_gradient(color1,color2)

    # color = [R,G,B]
    # grad = [[R,G,B],[R1,G1,B1],...[R254,G254,B24]]


    def create_gradient(self, color1, color2):
        grad = np.empty((256, 3), dtype="uint8")
        inc = (color2 - color1)/255
        value = color1.astype("float64")
        for i in range(256):
            grad[i] = value.astype("int8")
            value += inc
        return grad

#index int 0 - 255

    def get_color(self, index):
        return self.colormap[index]


#test
# RED = np.array([100, 0, 20])
#
# BLUE = np.array([0, 0, 255])
# print(ColorMap(RED, BLUE).colormap)