class FloatValue:
    @staticmethod
    def validate_float(value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate_float(value)
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.cells = [[Cell(0.0)] * m] * n


table = TableSheet(5, 3)
table.cells = [[Cell(float(i * table.m + j)) for j in range(1, table.m + 1)] for i in range(table.n)]