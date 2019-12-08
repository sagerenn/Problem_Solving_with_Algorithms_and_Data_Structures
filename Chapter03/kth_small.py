
import matplotlib.pyplot as plt 
import os 
from timeit import Timer
import random

def test1(n, k):
    n.sort()
    return n[k-1]

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots()
x_axis = []
y_axis = []

for i in range(10, 1001, 10):
    x = [random.randrange(i) for j in range(i)]
    t1 = Timer("test1(x, 10)", "from __main__ import x, test1")
    y = t1.timeit(number=1000)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='black')

plt.savefig("test.png")