names = ["Alice", "Betty", "Carol", "Daniel", "Ellen"]
target = "l"
names = [name for name in names if target in name]
print(names)