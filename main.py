class WordString:
    string: str

    def __init__(self, string=''):
        self.__string = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        if isinstance(value, str):
            self.__string = value

    def __len__(self):
        return len(self.string.split())

    def __call__(self, *args, **kwargs):
        return self.string.split()[args[0]]

