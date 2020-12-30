import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10)
y = np.random.rand(10)
plt.title("Title")
plt.xlabel("x - label")
plt.ylabel("y - label")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.grid()
plt.scatter(x, y, color="red", marker="x")
plt.show()
