"""
looking for exoplanets in kepler data

2013 (c) Christian Kohlstedde
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from copy import deepcopy
import os


sense = 10
width = 1
manFileList = ['kplr002571238-2009259160929']
filenames = os.listdir('data')
filenames.sort()
filenames = np.array(filenames)
filenames = np.core.defchararray.replace(filenames, '_llc.txt', '')


def median_filter(data, width):
    dataOrig = deepcopy(data)
    for position in xrange(len(data)):
        data[position, 1] = np.mean(
            dataOrig[abs(dataOrig[:, 0] - dataOrig[position, 0]) < width/2.0, 1]
        )


def research(dataOrig, filename):
    data = deepcopy(dataOrig)
    print 'data.size ', data.size, ' dataOrig.size', dataOrig.size
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
    print 'dt ', dt, ' period ', period

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

data = np.loadtxt('data/' + manFileList[0] + '_llc.txt')
research(data, manFileList[0])

first = True
for filename in filenames:
    file = 'data/' + filename + '_llc.txt'
    dataTemp = np.loadtxt(file)
    if(first):
        first = False
        data = np.array(deepcopy(dataTemp))
    else:
        data = np.concatenate([data, dataTemp])

research(data, 'all')
