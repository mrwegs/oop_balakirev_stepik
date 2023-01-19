import time


class WaterFilter:
    date: float

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and key in self.__dict__.keys():
            return
        super().__setattr__(key, value)


class Mechanical(WaterFilter):
    pass


class Aragon(WaterFilter):
    pass


class Calcium(WaterFilter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER: int = 100

    slot_1: Mechanical
    slot_2: Aragon
    slot_3: Calcium

    all_filters: dict

    def __init__(self):
        self.all_filters = {'1': None, '2': None, '3': None}

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def add_filter(self, slot_num, filter):
        if self.all_filters[str(slot_num)] is None and isinstance(filter, self.__annotations__.get(f'slot_{slot_num}')):
            self.all_filters[str(slot_num)] = filter

    def remove_filter(self, slot_num):
        self.all_filters[str(slot_num)] = None

    def get_filters(self):
        return self.all_filters.values()

    def water_on(self):
        for water_filter in self.all_filters.values():
            if not water_filter or time.time() - water_filter.date > self.MAX_DATE_FILTER:
                return False
        return True
