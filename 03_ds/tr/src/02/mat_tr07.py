import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 1000)
y = x.copy()
y[x < 0] = y[x < 0] * -1

plt.grid()
plt.plot(x, y)
plt.show()
