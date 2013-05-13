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

filename = 'data/kplr002571238-2009259160929_llc.txt'

data = np.loadtxt(filename)
dataOrig = deepcopy(data)

width = 1


def median_filter(data, width):
    for position in range(len(data)):
        cur_x = data[position, 0]
        new_y = 0
        count = 0
        for x in data[position:, 0]:
            if (x - cur_x) < (width / 2):
                new_y += data[position + count, 1]
                count += 1
            else:
                break
        new_y /= count
        count = 1
        for x in data[position::-1, 0]:
            if x == cur_x:
                continue
            if (cur_x - x) < (width / 2):
                new_y += data[position - count, 1]
                count += 1
            else:
                break
        new_y /= count
        data[position, 1] = new_y

plt.cla()
plt.plot(dataOrig[:,0], dataOrig[:,1])
plt.plot(data[:,0], data[:,1])
