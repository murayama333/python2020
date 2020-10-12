numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
file = "numbers.csv"
with open(file, "w") as f:
    for row in numbers:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")
