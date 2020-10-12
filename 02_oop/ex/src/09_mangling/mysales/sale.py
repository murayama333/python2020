class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")
