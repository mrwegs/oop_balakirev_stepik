class LessonItem:
    title: str
    practices: int
    duration: int

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if not isinstance(value, self.__annotations__.get(key)):
            raise TypeError('Неверный тип присваиваемых данных."')

        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        return


class Module:
    name: str
    lessons: list

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: LessonItem):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:
    name: str
    modules: list

    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module: Module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)


