prices = [1000, 2000, 3000]
discount_rate = 0.3
discounted_prices = [int(p - p * discount_rate) for p in prices]
print(discounted_prices)
