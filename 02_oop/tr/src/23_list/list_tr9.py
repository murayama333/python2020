my_range1 = range(1, 10)
my_range2 = range(1, 10, 3)
my_list = [v if v in my_range2 else "*" for v in my_range1]
print(my_list)
