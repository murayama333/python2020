class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x.get_value(), self.y.get_value())


class MyX:
    def get_value(self):
        return 10


class MyY:
    def get_value(self):
        return 20


if __name__ == "__main__":
    x = MyX()
    y = MyY()
    instance = MyClass(x, y)
    instance.myMethod(1)
