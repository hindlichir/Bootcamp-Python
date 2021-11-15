import numpy as np
from ImageProcessor import ImageProcessor
import copy


class ColorFilter:

    def invert(self, array):
        return 1 - array

    def to_blue(self, array):
        if len(array.shape) != 3:
            return None
        new_shape = (array.shape[0], array.shape[1], 2)
        new = np.zeros(new_shape, dtype='float32')
        return np.dstack((new, array[:, :, -1]))

    def to_green(self, array):
        if len(array.shape) != 3:
            return None
        new = copy.deepcopy(array)
        for i in [0, 2]:
            for x in range(0, array.shape[0]):
                for y in range(0, array.shape[1]):
                    new[x][y][i] = 0
        return new

    def to_red(self, array):
        return array - self.to_blue(array) - self.to_green(array)
