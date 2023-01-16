from typing import Union


class Circle:
    __x: Union[int, float]
    __y: Union[int, float]
    __radius: Union[int, float]

    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Неверный тип присваиваемых данных.')
        elif key == 'radius' and value < 0:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует