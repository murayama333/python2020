names1 = ["Alice", "Andy", "Bob", "Carol"]
names2 = ["Alice", "Betty", "Carol", "Charlie"]
names = list(set(names1 + names2))
names.sort()
print(names)
