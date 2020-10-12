target = input("Name: ")
file = "report.csv"
with open(file, "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    items = line.rstrip().split(",")
    if items[1] == target:
        print(items[0], items[2])
        total += int(items[2])
print("total", total)
