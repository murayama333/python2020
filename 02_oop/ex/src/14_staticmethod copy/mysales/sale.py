import datetime

class Sale:

    sale_count = 0

    def __init__(self, price, count):
        self.__price = price
        self.__count = count
        Sale.sale_count = Sale.sale_count + 1

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

    @classmethod
    def get_sale_count(cls):
        return cls.sale_count;

    @staticmethod
    def get_now():
        return datetime.datetime.now()
