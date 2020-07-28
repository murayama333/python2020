numbers_list = [[1, 2, 3, 4, 5],
                [10, 20, 30, 40, 50],
                [100, 200, 300, 400, 500]]

for numbers in numbers_list:
    sum = 0
    for number in numbers:
        sum += number
    print("Sum:", sum)
