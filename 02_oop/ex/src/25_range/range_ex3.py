def odd_generator(start=1, stop=10):
    for i in range(start, stop):
        if i % 2 == 1:
            yield i


og = odd_generator()
print(type(og))
for v in og:
    print(v)
