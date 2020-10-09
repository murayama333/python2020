def my_range(start, end, step=1):
    index = start
    while index < end:
        print("yield", index)
        yield index
        index += step


for i in my_range(1, 10):
    print(i)
