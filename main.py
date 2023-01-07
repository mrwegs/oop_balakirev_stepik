class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj: StackObj):
        if self.top:
            check_obj = self.top
            while check_obj.next is not None:
                check_obj = check_obj.next
            check_obj.next = obj
        else:
            self.top = obj

    def pop(self):
        if self.top and self.top.next:
            first = self.top
            second = first.next
            while second and second.next is not None:
                first = second
                second = first.next
            pop_item = second
            first.next = None
            return pop_item
        pop_item = self.top
        self.top = None
        return pop_item

    def get_data(self):
        res = list()
        check_obj = self.top
        while check_obj is not None:
            res.append(check_obj.data)
            check_obj = check_obj.next

        return res


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"