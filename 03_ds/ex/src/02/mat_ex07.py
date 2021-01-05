import numpy as np
import matplotlib.pyplot as plt

math = np.array([60, 70, 66, 88, 82, 75, 90, 72, 48, 52])
science = np.array([66, 64, 76, 92, 90, 75, 84, 70, 40, 48])

plt.title = "Score Report"
plt.xlabel = "math"
plt.ylabel = "science"
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid()
plt.scatter(math, science)
plt.show()