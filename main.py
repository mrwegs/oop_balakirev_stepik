class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            method = args[0].get('method', None) or 'GET'
            if method in self.methods:
                return self.__getattribute__(f'{method.lower()}')(func, args[0])
            return None

        return wrapper

    @staticmethod
    def get(func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    @staticmethod
    def post(func, request, *args, **kwargs):
        return f'POST: {func(request)}'