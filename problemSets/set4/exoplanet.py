"""
looking for exoplanets in kepler data

2013 (c) Christian Kohlstedde
"""

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ion()
from copy import deepcopy


sense = 10
width = 1
filenames = ['kplr002571238-2009259160929']


def median_filter(data, width):
    for position in range(len(data)):
        data[position, 1] = np.mean(
            data[abs(data[:, 0] - data[position, 0]) < 1, 1]
        )

for filename in filenames:
    file = 'data/' + filename + '_llc.txt'

    data = np.loadtxt(file)
    dataOrig = deepcopy(data)

    median_filter(data, 1)

    plt.cla()
    plt.scatter(dataOrig[:, 0], dataOrig[:, 1], s=1)
    plt.plot(data[:, 0], data[:, 1], 'r', lw=2)

    plt.savefig(filename + '-plot1.png')

    residualDataY = abs(dataOrig[:, 1] - data[:, 1])
    plt.cla()
    plt.plot(data[:, 0], residualDataY)

    plt.savefig(filename + '-plot2-residual.png')

    dt = np.diff(data[residualDataY > np.mean(residualDataY) * sense, 0])
    period = np.mean(dt[(dt > 1) & (dt < 15)])

    plt.cla()
    phaseX = ((data[:, 0]) % period) / period
    phaseX = ((data[:, 0]
              - np.mean(phaseX[residualDataY
                               > np.mean(residualDataY) * sense] - 0.5)
              * period) % period) / period

    plt.plot(phaseX, residualDataY)

    plt.savefig(filename + '-plot3-residual-phase.png')

    plt.cla()

    extract = (phaseX > 0.45) & (phaseX < 0.55)
    plt.plot(phaseX[extract], residualDataY[extract])
    plt.axis([0.45, 0.55, plt.axis()[2], plt.axis()[3]])

    plt.savefig(filename + '-plot4-residual-phase_extract.png')
