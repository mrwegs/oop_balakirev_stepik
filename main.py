class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        method = request.get('method', None)
        return f'GET: {self.func(request)}' if method in ('GET', None) else None

