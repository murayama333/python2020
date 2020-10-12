target = input("Subject: ")
file = "report.csv"
with open(file, "r") as f:
    lines = f.readlines()

math_total = 0
for line in lines:
    items = line.rstrip().split(",")
    if items[0] == target:
        math_total += int(items[2])
print("total", math_total)
