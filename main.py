from collections import Counter


class NewList:
    def __init__(self, lst: list = []):
        self.lst = lst

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError('Некорректный тип данных')
        other = other.lst if isinstance(other, self.__class__) else other
        other_types = [(n, type(n)) for n in other]
        result_list = list()
        for el in map(lambda x: (x, type(x)), self.lst):
            if el in other_types:
                other_types.remove(el)
            else:
                result_list.append(el[0])

        return self.__class__(result_list)

    def __rsub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise TypeError('Некорректный тип данных')
        other = other if isinstance(other, self.__class__) else self.__class__(other)
        return other - self

    def get_list(self):
        return self.lst
