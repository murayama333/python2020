names1 = ["Alice", "Andy", "Betty", "Bob", "Carol", "Charlie"]
names2 = ["Andy", "Betty", "Carol"]
names = [name for name in names1 if name not in names2]
print(names)