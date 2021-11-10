
class Vector:
    def __init__(self, values):
        self.values = values
        check = self._values
        if isinstance(check[0], list):
            i = len(check)
            j = 1
        else:
            i = 1
            j = len(check)
        self.shape = (i, j)

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, v):
        lst = []
        s = "The argument can either be a list, "
        s = s + "a list of list of floats, a size or a range"
        check_tuple = isinstance(v, tuple) and len(v) == 2
        if isinstance(v, int):
            for i in range(0, v):
                lst.append([float(i)])
            self._values = lst
        elif check_tuple and isinstance(v[0], int) and isinstance(v[0], int):
            for i in range(v[0], v[1]):
                lst.append([float(i)])
            self._values = lst
        elif isinstance(v, list):
            if (len(v) == 0):
                raise ValueError("The vector can't be an empty list")
            else:
                error = 0
                if isinstance(v[0], list) and len(v[0]) == 1:
                    for elem in v:
                        check = not isinstance(elem, list) or len(elem) != 1
                        if check or not isinstance(elem[0], float):
                            error = 1
                            break
                elif isinstance(v[0], float):
                    for elem in v:
                        if not isinstance(elem, float):
                            error = 1
                            break
                else:
                    error = 1
                if error == 0:
                    self._values = v
                else:
                    raise ValueError(s)
        else:
            raise ValueError(s)

    def __str__(self):
        s = f"The vector is {self._values} of shape {self.shape}."
        return s

    def __repr__(self):
        s = f"Vector(values={self._values}, shape={self.shape})"
        return s

    def __add__(self, other):
        if self.shape == other.shape:
            new = Vector(self._values)
            if isinstance(new.values[0], list):
                for i in range(0, len(new.values)):
                    new.values[i][0] = new.values[i][0] + other.values[i][0]
            else:
                for i in range(0, len(new.values)):
                    new.values[i] = new.values[i] + other.values[i]
            return new
        else:
            raise ValueError("Vectors need to be the same shape")

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        if self.shape == other.shape:
            new = Vector(self._values)
            if isinstance(new.values[0], list):
                for i in range(0, len(new.values)):
                    new.values[i][0] = new.values[i][0] - other.values[i][0]
            else:
                for i in range(0, len(new.values)):
                    new.values[i] = new.values[i] - other.values[i]
            return new
        else:
            raise ValueError("Vectors need to be the same shape")

    def __rsub__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if other == 0:
                raise ValueError("You cannot divide by zero!")
            else:
                new = Vector(self._values)
                if isinstance(new.values[0], list):
                    for i in range(0, len(new.values)):
                        new.values[i][0] = new.values[i][0] / other
                else:
                    for i in range(0, len(new.values)):
                        new.values[i] = new.values[i] / other
                return new
        else:
            raise ValueError("Vectors can only divided by a scalar")

    def __rtruediv__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            raise ValueError("What are you trying to do?")
        raise ValueError("A scalar cannot be divided by a Vector")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new = Vector(self._values)
            if isinstance(new.values[0], list):
                for i in range(0, len(new.values)):
                    new.values[i][0] = new.values[i][0] * other
            else:
                for i in range(0, len(new.values)):
                    new.values[i] = new.values[i] * other
            return new
        else:
            raise ValueError("Vectors can only divided by a scalar")

    def __rmul__(self, other):
        return self.__mult__(other)

    def dot(self, other):
        if self.shape == other.shape:
            new = Vector(self._values)
            if isinstance(new.values[0], list):
                for i in range(0, len(new.values)):
                    new.values[i][0] = new.values[i][0] * other.values[i][0]
            else:
                for i in range(0, len(new.values)):
                    new.values[i] = new.values[i] * other.values[i]
            return new
        else:
            raise ValueError("Vectors need to be the same shape")

    def T(self):
        new = []
        if isinstance(self.values[0], list):
            for i in range(0, len(self.values)):
                new.append(self.values[i][0])
        else:
            for i in range(0, len(self.values)):
                new.append([self.values[i]])
        return Vector(new)
