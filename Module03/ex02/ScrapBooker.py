import numpy as np


class ScrapBooker:

    def crop(self, array, dim, pos=(0, 0)):
        if not type(array).__module__ == np.__name__:
            return None
        if not isinstance(dim, tuple) or len(dim) != 2:
            return None
        elif not isinstance(dim[0], int) or not isinstance(dim[1], int):
            return None
        if not isinstance(pos, tuple) or len(pos) != 2:
            return None
        elif not isinstance(pos[0], int) or not isinstance(pos[1], int):
            return None
        range_x = range(pos[0], pos[0] + dim[0])
        range_y = range(pos[1], pos[1] + dim[1])
        matrix = [[array[x][y] for y in range_y] for x in range_x]
        return np.array(matrix)

    def thin(self, array, n, axis):
        if not type(array).__module__ == np.__name__:
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or (axis != 0 and axis != 1):
            return None
        if axis == 0 and n <= array.shape[1]:
            p = n - 1
            ran_x = range(0, array.shape[0])
            ran_y = range(0, array.shape[1])
            matrix = [[array[x][y] for y in ran_y if y != p] for x in ran_x]
            return np.array(matrix)
        elif axis == 1 and n <= array.shape[0]:
            p = n - 1
            ran_x = range(0, array.shape[0])
            ran_y = range(0, array.shape[1])
            matrix = [[array[x][y] for y in ran_y] for x in ran_x if x != p]
            return np.array(matrix)
        return None

    def juxtapose(self, array, n, axis):
        if not type(array).__module__ == np.__name__:
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or (axis != 0 and axis != 1):
            return None
        if axis == 0:
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            matrix = []
            for i in range(0, n):
                for x in range_x:
                    matrix.append([array[x][y] for y in range_y])
            return np.array(matrix)
        elif axis == 1:
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            matrix = []
            for x in range_x:
                matrix.append([array[x][y] for y in range_y] * n)
            return np.array(matrix)
        return None

    def mosaic(self, array, dim):
        if not type(array).__module__ == np.__name__:
            return None
        if not isinstance(dim, tuple) or len(dim) != 2:
            return None
        elif not isinstance(dim[0], int) or not isinstance(dim[1], int):
            return None
        matrix = []
        range_x = range(0, array.shape[0])
        range_y = range(0, array.shape[1])
        for i in range(0, dim[1]):
            for x in range_x:
                matrix.append([array[x][y] for y in range_y] * dim[0])
        return np.array(matrix)
