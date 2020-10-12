class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)


if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.myMethod(1)
