import matplotlib.pyplot as plt
import numpy as np

y = np.array([102, 56, 38, 12, 8, 77])
country = ["USA", "China", "Russia", "India", "brazil", "others"]

plt.pie(y, labels=country, startangle=90)
plt.show()