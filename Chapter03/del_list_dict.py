from timeit import Timer
import matplotlib.pyplot as plt
import os
import random

os.chdir(os.path.dirname( __file__))

# the x will reduce through the loop
del_list = Timer("del x[0]", "from __main__ import x")


fig, ax = plt.subplots()

x_axis = []
y_axis = []

for i in range(1000000, 10000001, 2000000):
    x = list(range(i))
    y = del_list.timeit(number=100)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='blue')


print(".............")
x_axis = []
y_axis = []
for i in range(1000000, 10000001, 2000000):
    x = {j:None for j in range(i)}
    avg = 0
    for j in range(100):
        del_dict = Timer("del x[%d]" % j, "from __main__ import x")
        y = del_dict.timeit(number=1)
        avg += y
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='red')

plt.savefig('test.png')