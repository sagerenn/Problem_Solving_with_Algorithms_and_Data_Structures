import matplotlib.pyplot as plt 
import os 
from timeit import Timer
import random

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots()
x_axis = []
y_axis = []

for i in range(10000, 1000001, 10000):
    x = {j:None for j in range(i)}
    t1 = Timer("x.get(%d)" % random.randrange(i), "from __main__ import i, x, random")
    y = t1.timeit(number=1000)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='blue', s=300)

x_axis = []
y_axis = []

for i in range(10000, 1000001, 10000):
    x = {j:None for j in range(i)}
    # x = dict(enumerate(list(range(i))))
    t1 = Timer("x[%d] = 5" % random.randrange(i), "from __main__ import x, random")
    y = t1.timeit(number=1000)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='green')

plt.savefig("test.png")