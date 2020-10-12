def count_down_generator():
    for i in range(5, -1, -1):
        yield i

for i in count_down_generator():
    print(i)
