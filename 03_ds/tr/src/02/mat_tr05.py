import numpy as np
import matplotlib.pyplot as plt

exam = np.loadtxt("exam.csv", delimiter=",", skiprows=1)
math = exam[:, 1]
english = exam[:, 2]

plt.boxplot([math, english], labels=["math", "english"])
plt.show()