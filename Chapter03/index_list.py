# x[i] --> O(1)

import matplotlib.pyplot as plt 
import os 
from timeit import Timer
import random

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots()
x_axis = []
y_axis = []

for i in range(10000, 100001, 10000):
    x = list(range(i))
    t1 = Timer("x[random.randrange(%d)]" % i, "from __main__ import x, random")
    y = t1.timeit(number=1000)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='blue')

plt.savefig("test.png")