class Sale:
    def __init__(self):
        self.price = 800
        self.count = 10

    def calc(self):
        return self.price * self.count

    def print(self):
        print(f"{self.calc():,d}")
