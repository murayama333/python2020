import numpy as np

a = np.arange(0, 6)
b = a.reshape(2, 3)
c = a.reshape(6, -1)
print(a)
print(b)
print(c)
