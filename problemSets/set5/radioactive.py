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
plt.cla()
from copy import deepcopy

data = np.loadtxt('decay_data.txt')
x = data[:, 0]
y = data[:, 1]
yerr = data[:, 2]


def radioactive(t, r_0, tau):
    return r_0 * np.exp(-t / tau)

popt, pcov = curve_fit(radioactive, x, y)

plt.cla()
plt.errorbar(x, y, yerr=yerr, fmt=None)
plt.plot(x, y)
plt.plot(x, radioactive(x, *popt))

print "radioactive = r_0 * np.exp(-t / tau)"
print "tau:", popt[1], "\tr_0:", popt[0]
print "uncertainties:"
print "tau:", pcov[1,1]**0.5, "\tr_0:", pcov[0,0]**0.5


def radioactive_real(t, r_0, tau, r_bkg):
    return r_0 * np.exp(-t / tau) + r_bkg

popt_real, pcov_real = curve_fit(radioactive_real, x, y)

plt.cla()
plt.errorbar(x, y, yerr=yerr, fmt=None)
plt.plot(x, y)
plt.plot(x, radioactive_real(x, *popt_real))

print ""
print "radioactive_real = r_0 * np.exp(-t / tau) + r_bkg"
print "tau:", popt_real[1], "\tr_0:", popt_real[0], "\tr_bkg", popt_real[2]
print "uncertainties:"
print "tau:", pcov_real[1,1]**0.5, "\tr_0:", pcov_real[0,0]**0.5, "\tr_bkg", pcov_real[2,2]**0.5
