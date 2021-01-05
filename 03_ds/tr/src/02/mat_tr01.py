import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 100)
y = - x**2

plt.grid()
plt.plot(x, y)
plt.show()
