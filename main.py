from random import randint # функция для генерации целых случайных значений в диапазоне [a; b]


class RandomPassword:
    psw_chars: str
    min_length: int
    max_length: int

    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        psw_length = randint(self.min_length, self.max_length)
        password = ''.join([self.psw_chars[randint(0, len(self.psw_chars)) - 1] for _ in range(psw_length)])
        return password


rnd = RandomPassword('qwertyuiopasdfghjklzxcvbnm0123456789', 5, 20)

lst_pass = [rnd() for _ in range(3)]




