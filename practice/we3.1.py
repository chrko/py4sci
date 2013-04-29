import numpy as np
import matplotlib.pyplot as plt


gaussian_values = np.random.normal(4.4, 1.2, 100000)

plt.ion()

plt.cla()
plt.hist(gaussian_values, normed=True)

