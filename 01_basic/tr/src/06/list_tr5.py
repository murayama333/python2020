items = [[300, 1], [200, 0], [100, 1], [500, 0], [400, 2]]

sum = 0
for item in items:
    price = item[0]
    number = item[1]
    sum += price * number

print("Sum:", sum)
