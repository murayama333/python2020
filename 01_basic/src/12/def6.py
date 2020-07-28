def recursion(x):
  if x < 10:
    print(x)
    recursion(x + 1)

recursion(1)