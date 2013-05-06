"""
looking for exoplanets in kepler data

2013 (c) Christian Kohlstedde
"""

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt


filename = 'data/kplr002571238-2009259160929_llc.txt'
f = open(filename, 'r')

line_count = 0
for x in open(filename):
    line_count += 1


data = np.zeros([line_count, 2])

i = 0

for line in f:
    line = line.strip()
    columns = line.split()
    data[i, 0] = float(columns[0])
    data[i, 1] = float(columns[1])
    i += 1
