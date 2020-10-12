my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
filter_keys = {"key1", "key3", "key5"}
print({key: value for key, value in my_dict.items() if key in filter_keys })
