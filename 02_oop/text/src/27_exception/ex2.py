x = int(input("X: "))
y = int(input("Y: "))
try:
    z = x / y
    print(z)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
