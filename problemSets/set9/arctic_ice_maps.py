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

from matplotlib.ticker import ScalarFormatter
import glob

data = np.load('ice_data/20080415.npy')

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

cax = ax.imshow(data, origin='lower', cmap=plt.cm.Blues_r)

fig.colorbar(cax)
ax.axis('off')

files = glob.glob('ice_data/*.npy')
files.sort()

pixels_above_50 = np.zeros([len(files), 2])
i = 0

for file in files:
    data = np.load(file)

    year = int(file[9:13])
    month = int(file[13:15])
    day	= int(file[15:17])

    time = year + (month - 1 + (day - 1) / 30.0) / 12.0

    pixels_above_50[i,0] = time
    pixels_above_50[i,1] = np.size(data[data >= 50])

    i = i + 1


fig = plt.figure()
ax = fig.add_subplot(111)
fig.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.plot(pixels_above_50[:,0], pixels_above_50[:,1])
ax.set_xlabel('Time')
ax.set_ylabel('pixel count')

fig = plt.figure()
ax = fig.add_subplot(111)
area = np.load('ice_data_area.npy')
cax = ax.imshow(area, origin='lower')
fig.colorbar(cax)
ax.axis('off')

covered_area = np.zeros([len(files), 3])
i = 0

for file in files:
    data = np.load(file)

    year = int(file[9:13])
    month = int(file[13:15])
    day = int(file[15:17])

    time = year + (month - 1 + (day - 1) / 30.0) / 12.0

    covered_area[i, 0] = time
    tmp = data / 100.0 * area
    covered_area[i, 1] = np.nansum(tmp)
    covered_area[i, 2] = np.sum(tmp[data > 99])

    i = i + 1


fig = plt.figure()
ax = fig.add_subplot(111)
fig.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
ax.plot(covered_area[:, 0], covered_area[:, 1])
ax.plot(covered_area[:, 0], covered_area[:, 2])

time = float(covered_area[covered_area[:,2]==np.min(covered_area[:,2]), 0])

year = int(time)
month = int((time - int(time)) * 12 + 1)
tmp = (time - int(time)) * 12 + 1
day = int((tmp - int(tmp)) * 30 + 1)

data2006 = np.load("ice_data/{year:04d}{month:02d}{day:02d}.npy".format(year=2006, month=month, day=day))
dataYear = np.load("ice_data/{year:04d}{month:02d}{day:02d}.npy".format(year=year, month=month, day=day))

fig = plt.figure()
ax1 = fig.add_subplot(121)
cax1 = ax1.imshow(data2006, origin='lower', cmap=plt.cm.Blues_r)
ax2 = fig.add_subplot(122)
cax2 = ax2.imshow(dataYear, origin='lower', cmap=plt.cm.Blues_r)
ax1.set_title('2006')
ax2.set_title(str(year))
ax1.axis('off')
ax2.axis('off')

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.imshow(dataYear - data2006, origin='lower', cmap=plt.cm.RdBu)
fig.colorbar(cax)
ax.axis('off')

files2006 = glob.glob('ice_data/2006*.npy')
files2011 = glob.glob('ice_data/2011*.npy')
files2006.sort()
files2011.sort()

data2006 = range(len(files2006))
for i in data2006:
    data2006[i] = np.load(files2006[i])

data2011 = range(len(files2011))
for i in data2011:
    data2011[i] = np.load(files2011[i])

data2006 = np.array(data2006)
data2011 = np.array(data2011)

data2006 = np.ma.masked_array(data2006,np.isnan(data2006))
data2011 = np.ma.masked_array(data2011,np.isnan(data2011))

mean2006 = np.mean(data2006, axis=0)
mean2011 = np.mean(data2011, axis=0)

mean2006 = mean2006.filled(np.nan)
mean2011 = mean2011.filled(np.nan)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
cax1 = ax1.imshow(mean2006, origin='lower', cmap=plt.cm.Blues_r)
cax2 = ax2.imshow(mean2011, origin='lower', cmap=plt.cm.Blues_r)
ax1.set_title('2006')
ax2.set_title('2011')
ax1.axis('off')
ax2.axis('off')
