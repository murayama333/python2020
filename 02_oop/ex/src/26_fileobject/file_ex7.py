file = "cities.csv"
with open(file, "r") as f:
    lines = f.readlines()
print("Total:", sum([int(line.split(",")[2].rstrip()) for line in lines]))
print("Max:", max([int(line.split(",")[2].rstrip()) for line in lines]))