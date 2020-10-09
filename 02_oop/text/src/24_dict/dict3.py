my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
try:
    value = my_dict["key1"]
    print(value, my_dict)
    value = my_dict["key10"]
    print(value, my_dict)
except KeyError as e:
    print(e)

value = my_dict.get("key1")
print(value, my_dict)
value = my_dict.get("key10", 10)
print(value, my_dict)

value = my_dict.pop("key1")
print(value, my_dict)

item = my_dict.popitem()
print(item, my_dict)
