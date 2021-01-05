import numpy as np
import matplotlib.pyplot as plt

exam = np.loadtxt("exam.csv", delimiter=",", skiprows=1)
math = exam[:, 1]
english = exam[:, 2]

figure = plt.figure()
ax1 = figure.add_subplot(2, 2, 1)
ax1.hist(math)

ax2 = figure.add_subplot(2, 2, 2)
ax2.scatter(math, english)

ax3 = figure.add_subplot(2, 2, 3)
ax3.scatter(english, math)

ax4 = figure.add_subplot(2, 2, 4)
ax4.hist(english)

plt.show()