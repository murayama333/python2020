users = [{"name": "Alice", "age": 19, "city": "London"},
         {"name": "Bob", "age": 20, "city": "Paris"},
         {"name": "Charlie", "age": 21, "city": "London"}]

print("Names:", end=" ")
for user in users:
    print(user["name"], end=" ")
print()
