class Money:
    def __init__(self, money):
        if self.check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, money):
        if self.__class__.check_money(money.__money):
            self.__money += money.__money

    @staticmethod
    def check_money(money):
        return isinstance(money, int) and money >= 0

