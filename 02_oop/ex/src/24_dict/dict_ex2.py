my_dict1 = {"key1": 1, "key2": 2, "key3": 3}
my_dict2 = {"key3": 30, "key4": 40, "key5": 50}

my_dict = {}
my_dict.update(my_dict1)
my_dict.update(my_dict2)
print(my_dict)
