
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
    def values(self, values):
        lst = []
        s = "The argument can either be a list, "
        s = s + "a list of list of floats, a size or a range"
        if isinstance(values, int):
            for i in range(0, values):
                lst.append([float(i)])
            self._values = lst
        elif isinstance(values, tuple) and len(values) == 2:
            for i in range(values[0], values[1]):
                lst.append([float(i)])
            self._values = lst
        elif isinstance(values, list):
            if (len(values) == 0):
                raise ValueError("The vector can't be an empty list")
            else:
                error = 0
                if isinstance(values[0], list) and len(values[0]) == 1:
                    for elem in values:
                        check = not isinstance(elem, list) or len(elem) != 1
                        if check or not isinstance(elem[0], float):
                            error = 1
                            break
                elif isinstance(values[0], float):
                    for elem in values:
                        if not isinstance(elem, float):
                            error = 1
                            break
                else:
                    error = 1
                if error == 0:
                    self._values = values
                else:
                    raise ValueError(s)
        else:
            raise ValueError(s)

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

