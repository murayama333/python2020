prices = [300, 200, 100, 500, 400]

sum = 0
for price in prices:
    sum += price
cnt = len(prices)
avg = sum // cnt

print("Sum:", sum)
print("Cnt:", cnt)
print("Avg:", avg)
