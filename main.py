class ImageFileAcceptor:
    extensions: tuple

    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        ext = args[0].rsplit('.')[-1]
        return ext in self.extensions



