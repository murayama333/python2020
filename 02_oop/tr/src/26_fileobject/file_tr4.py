file = "fruits.txt"
with open(file, "r") as f:
    lines = f.readlines()
print(sum([int(line.strip().split(" ")[1]) for line in lines]))
