"""
radioactive - not by The Imagine Dragons

2013 (c) Christian Kohlsteddde
"""

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.ion()

data = np.loadtxt('decay_data.txt')
x = data[:, 0]
y = data[:, 1]
yerr = data[:, 2]


def radioactive(t, r_0, tau):
    return r_0 * np.exp(-t / tau)

popt, pcov = curve_fit(radioactive, x, y, sigma=yerr)
y_line = radioactive(x, *popt)

plt.cla()
plt.errorbar(x, y, yerr=yerr, fmt=None)
plt.plot(x, y)
plt.plot(x, y_line)

print "radioactive = r_0 * np.exp(-t / tau)"
print "tau:", popt[1], "+/-", pcov[1, 1]**0.5
print "r_0:", popt[0], "+/-", pcov[0, 0]**0.5


def radioactive_real(t, r_0, tau, r_bkg):
    return r_0 * np.exp(-t / tau) + r_bkg

popt_real, pcov_real = curve_fit(radioactive_real, x, y, sigma=yerr)
y_line_real = radioactive_real(x, *popt_real)

plt.cla()
plt.errorbar(x, y, yerr=yerr, fmt=None)
plt.plot(x, y)
plt.plot(x, y_line_real)

print ""
print "radioactive_real = r_0 * np.exp(-t / tau) + r_bkg"
print "tau:\t", popt_real[1], "\t+/-", pcov_real[1, 1]**0.5
print "r_0:\t", popt_real[0], "\t+/-", pcov_real[0, 0]**0.5
print "r_bkg:\t", popt_real[2], "\t+/-", pcov_real[2, 2]**0.5


def chi(y, m, e):
    return np.sum(
        ((y - m) / e)**2
    ) / len(y)

print ""
print "chi for radioactive", chi(y, y_line, yerr)
print "chi for radioactive_real", chi(y, y_line_real, yerr)
