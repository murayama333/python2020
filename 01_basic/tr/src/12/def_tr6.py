def abs_sum(number_list):
    return sum([abs(n) for n in number_list])


numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9]
print(abs_sum(numbers))
