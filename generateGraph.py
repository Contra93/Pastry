import matplotlib.pyplot as plt
import numpy as np
import pylab
import math

f = open("results.txt", "r")
flist= f.read().split("\n")
xlist = []
ylist = []
relativedst = []
b = int(flist[0].split(" ")[6])
keySize = int(flist[0].split(" ")[10])
L = int(flist[0].split(" ")[14])
M = int(flist[0].split(" ")[18])

for i in range(0,len(flist)-1, 5):
    ylist.append(float(flist[i+2].split(" ")[2]))
    xlist.append(int(flist[i].split(" ")[2]))
    relativedst.append(float(flist[i+3].split(" ")[2]))
ylog = [math.log(o, 2**b) for o in xlist]

plt.figure(0)
x_axis = np.arange(0, 260, 20)
y_axis = np.arange(0, 5, 0.2)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(xlist, ylog, label = "log(N)")
plt.plot(xlist, ylist, label = "Pastry")
plt.xlabel('Number of nodes')
plt.ylabel('Average number of hops')
pylab.legend(loc = 'upper left')
plt.title("b = {}, keySize = {}, |L| = {}, |M| = {}, lookups = 200".format(b, keySize, L, M))
plt.show()

plt.figure(1)
hops = [0, 13, 54, 85, 44, 4, 0, 0, 0, 0, 0, 0, 0, 0]
x = list(range(0, len(hops)))
y = [o/200 for o in hops]
plt.bar(x, y)
plt.yticks(np.arange(0,1,0.05))
plt.xticks(x)
plt.xlabel('Number of hops')
plt.ylabel('Probability')
plt.title("b = {}, keySize = {}, |L| = {}, |M| = {}, lookups = 200".format(b, keySize, L, M))
plt.show()

plt.figure(2)
y_axis = np.arange(0, 2, 0.1)
plt.xticks(xlist)
plt.yticks(y_axis)
plt.plot(xlist, [round(o,1) for o in relativedst], label = "Pastry")
plt.plot(xlist, [1.0 for o in relativedst], label = "Complete routing table")
plt.xlabel('Number of nodes')
plt.ylabel('Relative Distance')
pylab.legend(loc = 'upper left')
plt.title("b = {}, keySize = {}, |L| = {}, |M| = {}, lookups = 200".format(b, keySize, L, M))
plt.show()

plt.figure(3)
x = ["No failure", "Failure with no \nrouting table repair", "Failure with routing\n table repair"]
y = [2.86, 2.95, 2.84]
plt.bar(x, y, width=0.5)
plt.yticks(np.arange(2,3.5,0.05))
plt.ylim([2.5,3.2])
plt.xticks(x)
plt.ylabel('Average hops per lookup')
plt.title('b = {}, keySize = {}, |L| = {}, |M| = {}, N = 200, failed Node = 40 (20% of total nodes), lookups = 200'.format(b, keySize, L, M), fontsize='small')
for a,b in zip(x, y):
    plt.text(a, b, str(b))
plt.show()

f.close()

f = open("NodeStatistics.txt", "r")
flist= f.read().split("\n")

# y1 -> Total node join time
# y2 -> Average node join time
# y3 -> Init time

x = []
y1 = []
y2 = []
y3 = []
for i in range(0, len(flist) - 1, 5):
    x.append(int(flist[i].split('=')[1].split(' ')[1]))
    y1.append(float(flist[i + 1].split(' ')[-1]))
    y2.append(float(flist[i + 2].split(' ')[-1]))
    y3.append(float(flist[i + 3].split(' ')[-1]))

plt.figure(4)
x_axis = np.arange(0, 220, 20)
y_axis = np.arange(0, 10, 1)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y1, label = "Total node join time")
plt.xlabel('Number of Nodes')
plt.ylabel('Total node join time')
pylab.legend(loc = 'upper left')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

plt.figure(5)
x_axis = np.arange(0, 220, 20)
y_axis = np.arange(0.040, 0.050, 0.0002)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y2, label = "Average node join time")
plt.xlabel('Number of Nodes')
plt.ylabel('Avg. node join time')
pylab.legend(loc = 'upper right')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

plt.figure(6)
x_axis = np.arange(0, 220, 20)
y_axis = np.arange(0, 36, 4)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y3, label = "Init time")
plt.xlabel('Number of Nodes')
plt.ylabel('Node initialization time')
pylab.legend(loc = 'upper left')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()
f.close()

f = open("PerformanceStatistics.txt", "r")
flist= f.read().split("\n")

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
for i in range(0, len(flist) - 1, 7):
    x.append(int(flist[i].split(':')[-1]))
    y1.append(float(flist[i + 1].split(':')[-1]))
    y2.append(float(flist[i + 2].split(':')[-1]))
    y3.append(float(flist[i + 3].split(':')[-1]))
    y4.append((float(flist[i + 4].split(':')[-1]) / 1024))
    y5.append(float(flist[i + 5].split(':')[-1]))

plt.figure(7)
x_axis = np.arange(0, 110, 10)
y_axis = np.arange(0, 7.5, 0.5)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y1, label = "Total User Time")
plt.plot(x, y3, label = "Total Process Time")
plt.xlabel('Number of Nodes')
plt.ylabel('Running Times')
pylab.legend(loc = 'upper left')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

plt.figure(8)
x_axis = np.arange(0, 110, 10)
y_axis = np.arange(0, 0.5, 0.05)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y2, label = "Total System Time")
pylab.legend(loc = 'upper left')
plt.xlabel('Number of Nodes')
plt.ylabel('Running Times')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

plt.figure(9)
x_axis = np.arange(0, 110, 10)
y_axis = np.arange(80, 1680, 100)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y4, label = "Total Memory")
pylab.legend(loc = 'upper left')
plt.xlabel('Number of Nodes')
plt.ylabel('Total Memory (KB)')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

plt.figure(10)
x_axis = np.arange(0, 110, 10)
y_axis = np.arange(6, 8, 0.1)
plt.xticks(x_axis)
plt.yticks(y_axis)
plt.plot(x, y5, label = "Total Wall clock time")
pylab.legend(loc = 'upper left')
plt.xlabel('Number of Nodes')
plt.ylabel('Total Wall clock time')
plt.title("b = 2, |L| = 8 |M| = 8")
plt.show()

f.close()
