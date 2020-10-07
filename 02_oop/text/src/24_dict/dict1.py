my_dict = {"key1": 1, "key2": 2, "key3": 3}
print(my_dict)

my_dict["key4"] = 4
print(my_dict)

value = my_dict.setdefault("key5", 5)
print(value)
print(my_dict)

value = my_dict.setdefault("key5", 55)
print(value)
print(my_dict)
