fruits = {
    "Apple": {"price": 100, "color": "Red"},
    "Banana": {"price": 200, "color": "Yellow"},
    "Cherry": {"price": 300, "color": "Red"},
}

redTotal = 0

for value in fruits.values():
    if value["color"] == "Red":
        redTotal += value["price"]

print(redTotal)
