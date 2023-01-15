class Telecast:
    def __init__(self, id, name, duration):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.indices = []

    def add_telecast(self, tl: Telecast):
        if isinstance(tl.uid, int) and tl.uid not in self.indices:
            self.items.append(tl)
            self.indices.append(tl.uid)

    def remove_telecast(self, indx: int):
        tl = list(filter(lambda x: x.uid == indx, self.items))[0]
        self.items.remove(tl)
        self.indices.remove(indx)

