def fizzbuzz_generator(start, stop):
    for i in range(start, stop):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield i

for i in fizzbuzz_generator(1, 16):
    print(i)
