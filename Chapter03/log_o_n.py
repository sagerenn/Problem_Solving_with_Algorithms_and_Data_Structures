# x[i] --> O(1)

import matplotlib.pyplot as plt 
import os 
from timeit import Timer

def test1(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots()
x_axis = []
y_axis = []

for i in range(1000000, 1000000001, 1000000):
    t1 = Timer("test1(%d)" % i, "from __main__ import test1")
    y = t1.timeit(number=1000)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='green')

plt.savefig("test.png")