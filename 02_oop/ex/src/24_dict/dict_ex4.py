my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
while len(my_dict):
    key, value = my_dict.popitem()
    print(key, value)