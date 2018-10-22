import matplotlib.pyplot as plt
import numpy as np

x = [2, 3, 4, 5, 6, 7]
y = "np.add(np.multiply(x, 5), -np.power(x, 2))"
y1 = "3.0 + np.multiply(x, 3)"
y2 = "np.add(x, -5)"

plt.plot(x, eval(y2))
plt.show()
