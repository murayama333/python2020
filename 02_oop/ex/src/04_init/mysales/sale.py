class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")
