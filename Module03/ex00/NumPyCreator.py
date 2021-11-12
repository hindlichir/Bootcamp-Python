from typing import Iterable
import random
import numpy


class NumPyCreator:
    def from_list(self, lst, *args):
        if args:
            return None
        if not isinstance(lst, list):
            return None
        else:
            if lst and isinstance(lst[0], list):
                length_check = len(lst[0])
                for elem in lst:
                    if not isinstance(elem, list):
                        return None
                    if len(elem) != length_check:
                        return None
            else:
                for elem in lst:
                    if hasattr(elem, '__iter__') and not isinstance(elem, str):
                        return None
        return numpy.array(lst)

    def from_tuple(self, tpl, *args):
        if args:
            return None
        if not isinstance(tpl, tuple):
            return None
        else:
            if tpl and isinstance(tpl[0], tuple):
                length_check = len(tpl[0])
                for elem in tpl:
                    if not isinstance(elem, tuple):
                        return None
                    if len(elem) != length_check:
                        return None
            else:
                for elem in tpl:
                    if hasattr(elem, '__iter__') and not isinstance(elem, str):
                        return None
        return numpy.array(tpl)

    def from_iterable(self, itr, *args):
        if args:
            return None
        if not isinstance(itr, Iterable):
            raise TypeError("The argument is not a tuple.")
        else:
            if itr and isinstance(itr[0], Iterable):
                length_check = len(itr[0])
                for elem in itr:
                    if not isinstance(elem, Iterable):
                        return None
                    if len(elem) != length_check:
                        return None
            else:
                for elem in itr:
                    if hasattr(elem, '__iter__') and not isinstance(elem, str):
                        return None
        return numpy.array(itr)

    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple) or len(shape) != 2:
            return None
        matrix = [[value for x in range(shape[1])] for y in range(shape[0])]
        return numpy.array(matrix)

    def random(self, shape):
        if not isinstance(shape, tuple) or len(shape) != 2:
            return None
        r, c = range(shape[0]), range(shape[1])
        matrix = [[random.random() for x in c] for y in r]
        return numpy.array(matrix)

    def identity(self, n):
        if not isinstance(n, int):
            return None
        array = self.from_shape((n, n), 0.)
        for i in range(n):
            array[i, i] = 1
        return array
