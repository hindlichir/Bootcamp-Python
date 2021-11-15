import numpy as np


class ScrapBooker:

    def crop(self, array, dim, pos=(0,0)):
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
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            matrix = [[array[x][y] for y in range_y if y != p] for x in range_x]
            return np.array(matrix)
        elif axis == 1 and n <= array.shape[0]:
            p = n - 1
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            matrix = [[array[x][y] for y in range_y] for x in range_x if x != p]
            return np.array(matrix)
        return None      
            

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if not type(array).__module__ == np.__name__:
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        if not isinstance(axis, int) or (axis != 0 and axis != 1):
            return None
        if axis == 0:
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            range_i = range(0, array.shape[1] * n)
            matrix = []
            for x in range_x:
                for i, y in range_i, range_y:
                    matrix[x][i * n + y] = array[x][y]
            return np.array(matrix)
        elif axis == 1:
            range_x = range(0, array.shape[0])
            range_y = range(0, array.shape[1])
            range_i = range(0, array.shape[1] * n)
            matrix = []
            for x in range_x:
                for i in range(0, n):
                    for y in range_y:
                        matrix[i * n + x][y] = array[x][y]
            return np.array(matrix)
        return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
print(spb.thin(arr2,3,0))

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))