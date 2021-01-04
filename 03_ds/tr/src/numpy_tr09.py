import numpy as np

array = np.arange(1, 101).reshape(10, -1)

print(array[:, -1].reshape(-1, 1))
