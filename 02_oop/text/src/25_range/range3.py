class MyRange:
    def __init__(self, start, stop, step=1):
        self.index = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.stop:
            raise StopIteration()
        value = self.index
        self.index += 1
        return value


my_range = MyRange(1, 10)
for i in my_range:
    print(i)
