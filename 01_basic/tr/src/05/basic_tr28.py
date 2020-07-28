prices = [300, 200, 100, 500, 400]
numbers = [1, 0, 1, 0, 2]

sum = 0
for price, number in zip(prices, numbers):
    sum += price * number

print("Sum:", sum)
