class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: int = 0, y: int = 0):
        if isinstance(x, (int, float)) \
                and isinstance(y, (int, float)) \
                and self.MIN_COORD <= x <= self.MAX_COORD \
                and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__x = x
            self.__y = y
        else:
            self.__x = 0
            self.__y = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2

