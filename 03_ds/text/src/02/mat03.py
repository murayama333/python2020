import numpy as np
import matplotlib.pyplot as plt

x = np.array([50, 25, 10, 10, 5])
plt.pie(x, counterclock=False, startangle=90)
plt.show()
