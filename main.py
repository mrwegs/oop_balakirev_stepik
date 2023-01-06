class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        if self.__next is None:
            self.__next = obj
        else:
            self.__next.set_next(obj)

    def set_prev(self, obj):
        if self.__prev is None:
            self.__prev = obj
        else:
            self.__prev.set_prev(obj)

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj: ObjList):
        if self.head is None:
            self.head = obj
        elif self.tail is None:
            self.tail = obj
            self.head.set_next(obj)
            self.tail.set_prev(self.head)
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail is None:
            self.head = None
            return
        new_tail = self.tail.get_prev()
        new_tail.set_next = None
        self.tail = new_tail

    def get_data(self):
        data_list = []
        obj = self.head
        if obj:
            data_list.append(obj.get_data())
            while obj.get_next() is not None:
                obj = obj.get_next()
                data_list.append(obj.get_data())

        return data_list


