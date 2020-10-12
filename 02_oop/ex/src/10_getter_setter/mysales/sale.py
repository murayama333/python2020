class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count
