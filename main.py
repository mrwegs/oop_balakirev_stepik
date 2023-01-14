class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    def get_total_weight(self):
        if self.things:
            return sum([thing.weight for thing in self.__things])
        return 0

    @property
    def things(self):
        return self.__things

    @things.setter
    def things(self, value):
        self.__things = value

    def add_thing(self, thing: Thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.things.append(thing)

    def remove_thing(self, indx):
        if self.things:
            self.things.pop(indx)

