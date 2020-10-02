class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count
