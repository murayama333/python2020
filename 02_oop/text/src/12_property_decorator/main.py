class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


if __name__ == "__main__":
    instance = MyClass(10, 20)
    instance.x = 100
    instance.y = 200
    instance.myMethod(1)
    print(instance.x)
    print(instance.y)
