class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)


if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.__x = 100
    instance.__y = 200
    instance.myMethod(1)

    instance._MyClass__x = 100
    instance._MyClass__y = 200
    instance.myMethod(1)
