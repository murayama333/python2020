class Sale:
    def __init__(self, price, count):
        self.__price = price
        self.__count = count

    def calc(self):
        return self.__price * self.__count

    def print(self):
        print(f"{self.calc():,d}")


class Customer:
    def __init__(self, name):
        self.__name = name

    def print(self):
        print(f"{self.__name}")


class CustomerSale:
    def __init__(self, customer, sale):
        self.customer = customer
        self.sale = sale

    def print(self):
        self.customer.print()
        self.sale.print()
