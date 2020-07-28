price = int(input("PRICE: "))
member = input("MEMBER: ")

if member == "GOLD":
    point = price // 500
else:
    point = price // 1000

if point > 0:
    print("POINT:", point)
