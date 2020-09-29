class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)


if __name__ == "__main__":
    instance = MyClass()
    instance.myMethod(1)
