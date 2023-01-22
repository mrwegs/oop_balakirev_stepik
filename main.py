class InputValues:
    def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
        self.render = render

    def __call__(self, func):     # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            number_list = list(map(self.render, func().split()))
            return number_list
        return wrapper


class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None


@InputValues(RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)



