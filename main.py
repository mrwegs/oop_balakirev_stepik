class Product:
    __ID = 0

    id: int
    name: str
    weight: (int, float)
    price: (int, float)

    def __init__(self, name, weight, price):
        self.id = Product.set_id()
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key)) or (key in ('price', 'weight') and value < 0):
            raise TypeError('Неверный тип присваиваемых данных.')

        super().__setattr__(key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")

        super().__delattr__(item)

    @classmethod
    def set_id(cls):
        cls.__ID += 1
        return cls.__ID


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)
