import numpy as np
import matplotlib.pyplot as plt

count = 100
x = np.random.rand(count)
# x = np.random.randn(count)
plt.hist(x)
plt.show()
