import random as r
from string import ascii_lowercase, ascii_uppercase, digits
import re


class EmailValidator:
    ALLOW_SYMBOLS = ascii_uppercase + ascii_lowercase + digits + '.' + '_'

    __instance = None

    def __new__(cls, *args, **kwargs):
        return cls.__instance

    @classmethod
    def get_random_email(cls):
        n = r.randint(1, 20)
        name = r.choices(cls.ALLOW_SYMBOLS, k=n)
        return ''.join(name) + '@gmail.com'

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        pattern = r'((\w)(\.?)){1,100}@(\w+\.[a-z]+){1,50}'
        match = re.fullmatch(pattern, email)
        return bool(match)

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
