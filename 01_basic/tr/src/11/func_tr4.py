numbers_tuple = ((10, 20, 30), (40, 50, 60), (70, 80, 90))
print(sum([n for ns in numbers_tuple for n in ns]))
