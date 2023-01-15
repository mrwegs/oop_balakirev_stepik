class Book(object):
    title: str
    author: str
    pages: int
    year: int

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key)):
            raise TypeError("Неверный тип присваиваемых данных.")

        super().__setattr__(key, value)


book = Book(author='Сергей Балакирев', title='Python ООП', pages=123, year=2022)

