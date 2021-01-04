import numpy as np

np.random.seed(3)
array = np.random.randn(1000)

print("Mean:", array.mean())
print("Std:", array.std())
print("Count:", len(array))
