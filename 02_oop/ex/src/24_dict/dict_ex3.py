my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
except_keys = ["key1", "key3", "key5"]
my_dict2 = {key: value for key, value in my_dict.items() if key not in except_keys}
print(my_dict2)
