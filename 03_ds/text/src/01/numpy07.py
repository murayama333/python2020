import numpy as np

a = np.arange(0, 100).reshape(10, 10)
print(a)
print(a[1])
print(a[1, 1])
print(a[1:5, 1:5])
print(a[:, 1])
