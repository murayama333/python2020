fruits = {
    "Apple": {"price": 100, "color": "Red"},
    "Banana": {"price": 200, "color": "Yellow"},
    "Cherry": {"price": 300, "color": "Red"},
}

for key, value in fruits.items():
    if value["color"] == "Red":
        print(key)
