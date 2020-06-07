print("PRICE:", end="")
price = int(input())
print("MEMBER:", end="")
member = input()

if member == "GOLD" :
  point = int(price / 500)
else:
  point = int(price/ 1000)

if point > 0:
  print("POINT:", end="")
  print(point)
