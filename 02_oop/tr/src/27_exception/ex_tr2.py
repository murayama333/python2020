target_key = input("Key: ")
try:
    my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
    print(my_dict[target_key])
except:
    print(f"{target_key} is not found.")
