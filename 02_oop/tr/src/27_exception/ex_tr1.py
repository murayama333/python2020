try:
    x = int(input("x: "))
    y = int(input("y: "))
    z = x + y
    print(f"{x}+{y}={z}")
except ValueError as e:
    print("ERROR")
