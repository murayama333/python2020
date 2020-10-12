my_list1 = ["c", "d"]
my_list2 = ["a", "b"]
my_list3 = ["e"]
my_list = my_list1 + my_list2 + my_list3
my_list.sort()
print("".join([e.upper() for e in my_list]))
