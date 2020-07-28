def double(x):
  return 2 * x

def array_double(list):
  result = []
  for i in list:
    result.append(double(i))
  return result

prices = [100, 200, 300]
result = array_double(prices)
print(result)