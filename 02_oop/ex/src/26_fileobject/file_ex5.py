file = "cities.csv"
with open(file, "r") as f:
    lines = f.readlines()
for line in lines:
    index, name, population = line.split(",")
    print(name)
