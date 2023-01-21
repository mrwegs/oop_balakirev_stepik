class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        number = args[0]
        try:
            return int(number)
        except ValueError:
            return None

