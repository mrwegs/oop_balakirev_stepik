from string import ascii_lowercase, digits


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator
class LengthValidator:
    __min_length: int
    __max_length: int

    def __init__(self, min_length, max_length):
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        string = args[0]
        return len(string) in range(self.__min_length, self.__max_length + 1)


class CharsValidator:
    __chars: str

    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        string = args[0]
        return all(c in self.__chars for c in string)
