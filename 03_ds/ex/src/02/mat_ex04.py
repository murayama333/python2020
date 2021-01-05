import numpy as np
import matplotlib.pyplot as plt

sales = np.array([10000, 5000, 3000, 1000, 1000])
sales_label = np.array(["Item A", "Item B", "Item C", "Item D", "Item E"])

plt.pie(sales, counterclock=False, startangle=90, labels=sales_label)
plt.show()