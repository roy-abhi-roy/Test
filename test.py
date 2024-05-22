import numpy as np

import matplotlib.pyplot as plt

print("Thanks Dan")

x = np.linspace(0, 2 * np.pi, 100)
print(x)
y = np.sin(x)

plt.plot(x, y)
plt.show()
