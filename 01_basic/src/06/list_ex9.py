names = ["Alice", "Bob"]

name = names[0]
names[0] = names[1]
names[1] = name

# names[0], names[1] = names[1], names[0]

print(names)
