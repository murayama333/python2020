class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.x, self.y)


class MySubClass(MyClass):
    def myMethod2(self):
        print("call myMethod2")


if __name__ == "__main__":
    instance = MySubClass(10, 20)
    instance.myMethod(1)
    instance.myMethod2()
