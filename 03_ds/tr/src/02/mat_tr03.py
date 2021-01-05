import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 8, 100)
y = np.log2(x)

plt.grid()
plt.plot(x, y)
plt.show()