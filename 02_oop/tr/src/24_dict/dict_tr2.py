my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
filter_key = "key3"
print({key: value for key, value in my_dict.items() if key == filter_key })
