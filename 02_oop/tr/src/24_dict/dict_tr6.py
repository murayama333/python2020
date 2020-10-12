my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
while True:
    if len(my_dict) == 0:
        break
    print(my_dict.popitem())
