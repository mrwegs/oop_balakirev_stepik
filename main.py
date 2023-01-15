class AppVK:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self, name='ВКонтакте'):
        self.name = name


class AppYouTube:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self, max_size, name='YouTube'):
        self.name = name
        self.max_size = max_size


class AppPhone:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return super().__new__(cls)
        return cls.__instance

    def __init__(self, phone_list, name='Phone'):
        self.name = name
        self.phone_list = phone_list


class SmartPhone:
    model: str
    apps: list

    def __init__(self, model):
        self.model = model

    def add_app(self, app):
        self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)

