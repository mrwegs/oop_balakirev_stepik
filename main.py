from typing import Union, Any


class ObjList:
    __data: str
    __prev: Any
    __next: Any

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    __head: Union[ObjList, None]
    __tail: Union[ObjList, None]
    __objects: list

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__objects = list()
        
    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self, value):
        self.__head = value
        
    @property
    def tail(self):
        return self.__tail
    
    @tail.setter
    def tail(self, value):
        self.__tail = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        self.__objects = value

    def add_obj(self, obj: ObjList):
        self.objects.append(obj)

        if self.head is None:
            self.head = self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        obj: ObjList = self.objects[indx]
        if len(self.objects) == 1:
            self.head = self.tail = None
        elif obj is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        elif obj is self.head:
            self.head = obj.next
            self.head.prev = None
        else:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev

        self.objects.pop(indx)

    def __len__(self):
        return len(self.objects)

    def __call__(self, *args, **kwargs):
        return self.objects[args[0]].data

