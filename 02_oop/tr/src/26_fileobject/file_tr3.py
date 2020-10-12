fruits = {"Apple": 100, "Lemon": 200, "Oragne": 300}
file = "fruits.txt"
with open(file, "w") as f:
    for name, price in fruits.items():
        f.write(f"{name} {price}\n")
