class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        input_numbers = self.func()
        return list(map(int, input_numbers.split()))


input_dg = InputDigits(input)
res = input_dg()


