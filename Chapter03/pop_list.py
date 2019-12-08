from timeit import Timer
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

# the x will reduce through the loop
pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")


fig, ax = plt.subplots()

x_axis = []
y_axis = []

for i in range(1000000, 10000001, 2000000):
    x = list(range(i))
    y = pop_zero.timeit(number=100)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='blue')


print(".............")
x_axis = []
y_axis = []
for i in range(1000000, 10000001, 2000000):
    x = list(range(i))
    y = pop_end.timeit(number=100)
    x_axis.append(i)
    y_axis.append(y)

ax.scatter(x_axis, y_axis, c='red')

plt.savefig('test.png')