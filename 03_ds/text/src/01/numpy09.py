import numpy as np

a = np.array([80, 60, 30, 70, 40])
print(a < 50)

a[a < 50] = 0
print(a)
