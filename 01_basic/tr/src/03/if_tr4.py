x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))

max = 0
if x > y:
    if x > z:
        max = x
    else:
        max = z
else:
    if y > z:
        max = y
    else:
        max = z

print("Max", max)
