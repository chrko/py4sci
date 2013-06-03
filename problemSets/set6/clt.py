"""
The Central Limit Theorem (CLT)

2013 (c) Christian Kohlsteddde
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'true':
    interactive = True
else:
    interactive = False
import numpy as np
import matplotlib
if not interactive:
    matplotlib.use('Agg')
import matplotlib.pyplot as plt
if interactive:
    plt.ion()

import scipy.interpolate as ip
import scipy.integrate as ig


def sample(x, p, n):
    # Calc the integral of p
    intg = ig.simps(p, x=x)
    # Checking the normed
    if np.abs(intg) - 1 > 0.00001:
        # Norm p
        p = p / ig.simps(p, x=x)
    # Getting n values between 0 and 1
    i = np.random.random(n)
    C = ip.interp1d(np.hstack([0., ig.cumtrapz(p, x=x)]), x)
    return C(i)

data = np.loadtxt('pdf_data.txt')
x = data[:, 0]
p = data[:, 1]

# Norm p
p_normed = p / ig.simps(p, x=x)

samples = sample(x, p, 10000)

plt.cla()
plt.plot(x, p_normed)
plt.hist(samples, normed=True, bins=100)

plt.savefig('1.png')


def sample_iter(x, p, n, m):
    values = np.array([])
    for i in range(m):
        values = np.hstack([values, sample(x, p, n)])
    return np.sum(np.reshape(values, [n, m]), axis=1)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

n = 10000
bins = 100
ax1.hist(sample_iter(x, p, n, 1), normed=True, bins=bins)
ax2.hist(sample_iter(x, p, n, 3), normed=True, bins=bins)
ax3.hist(sample_iter(x, p, n, 9), normed=True, bins=bins)
ax4.hist(sample_iter(x, p, n, 27), normed=True, bins=bins)

plt.savefig('2.png')
