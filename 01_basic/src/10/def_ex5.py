def factorial(x):
  if x > 1:
    return x * factorial(x - 1)
  return 1

x = 5
y = factorial(x)
print(y)
