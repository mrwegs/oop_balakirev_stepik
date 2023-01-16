class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    __a: (int, float)
    __b: (int, float)
    __c: (int, float)

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value in range(self.MIN_DIMENSION, self.MAX_DIMENSION + 1):
            self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError('Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.')
        super().__setattr__(key, value)

