file = "numbers.csv"
with open(file, "r") as f:
    lines = f.readlines()

total = 0
for line in lines:
    items = [int(item) for item in line.split(",")]
    total += sum(items)
print(total)
