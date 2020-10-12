cities = [{"index": 1, "name": "Tokyo", "population": 927},
          {"index": 2, "name": "London", "population":  898},
          {"index": 3, "name": "New York", "population": 834}]
file = "cities.csv"
with open(file, "w") as f:
    for city in cities:
        f.write(f"{city['index']},{city['name']},{city['population']}\n")
