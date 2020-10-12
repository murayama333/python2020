file = "cities.csv"
with open(file, "r") as f:
    lines = f.readlines()
for line in lines:
    print(line, end="")
