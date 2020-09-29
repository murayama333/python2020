class MyClass:

    a = 1000

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def myMethod(self, arg1):
        print("call myMethod", arg1, self.__x, self.__y)

    @classmethod
    def myClassMethod(cls, arg1):
        print("call myClassMethod", arg1, cls.a)

    @staticmethod
    def myStaticMethod(arg1):
        print("call myStaticMethod", arg1)


if __name__ == "__main__":
    instance = MyClass(100, 200)
    instance.myMethod(1)
    MyClass.myClassMethod(10)
    MyClass.myStaticMethod(100)
