x = input("X: ")
y = input("y: ")

if x == "G" and y == "C" or x == "C" and y == "P" or x == "P" and y == "G":
    print("Win: X")
elif x == "G" and y == "P" or x == "C" and y == "G" or x == "P" and y == "C":
    print("Win: Y")
else:
    print("Draw")
