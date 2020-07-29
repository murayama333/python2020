names = ("Apple", "Banana", "Lemon", "Apple", "Lemon")
target = input("Target: ")
count = 0
for name in names:
    if name == target:
        count += 1
print("Count:", count)
