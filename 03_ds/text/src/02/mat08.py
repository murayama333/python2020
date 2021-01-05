import numpy as np
import matplotlib.pyplot as plt

x = ["A", "B", "C", "D", "E"]
y = np.array([50, 25, 10, 10, 5])

figure = plt.figure()

axes1 = figure.add_subplot(1, 2, 1)
axes1.bar(x, y)

axes2 = figure.add_subplot(1, 2, 2)
axes2.pie(y, labels=x, counterclock=False, startangle=90)

plt.show()
