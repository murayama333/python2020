my_dict = {"key1": 1, "key2": 2, "key3": 3}
all_keys = ["key1", "key2" ,"key3", "key4", "key5"]
for key in all_keys:
    my_dict.setdefault(key, 0)
print(my_dict)
