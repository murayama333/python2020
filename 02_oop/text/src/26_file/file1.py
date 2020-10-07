names = ["Alice", "Bob", "Charlie"]
f = open("names.txt", mode="w")
for name in names:
    f.write(name + "\n")
f.close()
