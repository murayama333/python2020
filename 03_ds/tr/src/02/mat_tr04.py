import numpy as np
import matplotlib.pyplot as plt

x1 = [65, 76, 65, 70, 66]
y1 = [170, 182, 175, 178, 168]

x2 = [75, 76, 82, 70, 72]
y2 = [178, 185, 182, 172, 176]

plt.scatter(x1, y1, marker="o", color="red")
plt.scatter(x2, y2, marker="x", color="blue")

plt.show()