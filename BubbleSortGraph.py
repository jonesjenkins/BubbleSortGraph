import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng

rng = default_rng()
y = rng.choice(20, size=20, replace=False)
x = np.arange(len(y))
ax = plt.axes()
ax.set_facecolor("black")
plt.stem(x, y, use_line_collection=True)
plt.pause(.001)
plt.cla()
for i in range(len(y)):
    for j in range(0, len(y) - i - 1):
        if y[j] > y[j + 1]:
            y[j], y[j + 1] = y[j + 1], y[j]
        plt.stem(x, y, use_line_collection=True)
        plt.pause(.001)
        plt.cla()