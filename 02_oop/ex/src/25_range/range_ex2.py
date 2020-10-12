class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.lst):
            raise StopIteration()
        index = self.i
        value = self.lst[index]
        self.i += 1
        return index, value


names = ["Alice", "Bob", "Carol"]
for i, v in MyIterator(names):
    print(i, v)
