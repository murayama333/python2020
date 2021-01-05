import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = 2 ** x

plt.grid()
plt.plot(x, y)
plt.show()