from random import randint

def random_list():
  size = randint(1, 9)
  return list(range(size))

list = random_list()
print(list)
