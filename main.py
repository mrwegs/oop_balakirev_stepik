class PhoneNumber:
    def __init__(self, number: int, fio: str):
        self.number = number if self.check_phone(number) else 00000000000
        self.fio = fio

    @staticmethod
    def check_phone(phone: int):
        return len(str(phone)) == 11 and isinstance(phone, int)


class PhoneBook:
    def __init__(self):
        self.phone_list = list()

    def add_phone(self, phone: PhoneNumber):
        self.phone_list.append(phone)

    def remove_phone(self, indx):
        self.phone_list.pop(indx)

    def get_phone_list(self):
        return self.phone_list

