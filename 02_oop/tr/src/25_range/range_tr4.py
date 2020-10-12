class AlphabetIterator:
    def __init__(self, upper=False):
        if upper:
            self.code = 65
        else:
            self.code = 97
        self.end_code = self.code + 26

    def __iter__(self):
        return self

    def __next__(self):
        if self.code == self.end_code:
            raise StopIteration()
        value = bytes([self.code]).decode("UTF-8")
        self.code += 1
        return value


for v in AlphabetIterator(upper=True):
    print(v, end="")
print()

for v in AlphabetIterator(upper=False):
    print(v, end="")
print()