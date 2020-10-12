names = ["Alice", "Betty", "Carol", "Daniel", "Ellen"]
target = "l"
names = [name for name in names if target == name[len(name) - 1]]
print(names)