class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return isinstance(string, str) and len(string) in range(self.min_length, self.max_length + 1)


class StringValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'''<form>
        Логин: {self.login}
        Пароль: {self.password}
        Email: {self.email}
        </form>''')
