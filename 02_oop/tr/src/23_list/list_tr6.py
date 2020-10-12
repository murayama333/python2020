my_list1 = ["one", "three", "five"]
my_list2 = ["two", "four", "six"]
my_list = []
for name1, name2 in zip(my_list1, my_list2):
    my_list.append(name1)
    my_list.append(name2)
print(my_list)
