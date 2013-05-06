"""
looking for exoplanets in kepler data

2013 (c) Christian Kohlstedde
"""

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ion()


filename = 'data/kplr002571238-2009259160929_llc.txt'

data = np.loadtxt(filename)
dataOrig = data

width = 1

for position in range(len(data)):
    startday = data[position,0]

    count = 0
    median = 0
    for day in data[position:,0]:
        if (day - startday) < width:
	    median += data[position+count,1]
	    count += 1
        else:
	    break
    median /= count
    data[position, 1] = median

plt.cla()
plt.plot(dataOrig[:,0], dataOrig[:,1])
plt.plot(data[:,0], data[:,1])
