import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

X = loadmat('ex7data1.mat')['X']

ax = plt.subplot(1, 1, 1)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.plot(X[:, 0], X[:, 1], 'o', color='black', markerfacecolor='none')
ax.axis('square')

plt.show()
