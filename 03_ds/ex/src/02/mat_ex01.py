import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
x = np.random.randn(1000)

plt.hist(x)
plt.show()