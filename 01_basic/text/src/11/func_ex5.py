from random import randint

x = int(input("Please enter a number (0:Goo, 1:Choki, 2:Par) "))
y = randint(0, 2)
print("Computer", y)
if x == 0 and y == 1 \
        or x == 1 and y == 2 \
        or x == 2 and y == 0:
    print("Win")
elif x == 0 and y == 2 \
        or x == 1 and y == 0 \
        or x == 2 and y == 1:
    print("Lose")
else:
    print("Draw")
