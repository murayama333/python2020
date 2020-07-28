x = int(input("X: "))
y = int(input("y: "))

for i in range(x):
    for j in range(y):
        print((i + 1) * (j + 1), end=" ")
    print()
