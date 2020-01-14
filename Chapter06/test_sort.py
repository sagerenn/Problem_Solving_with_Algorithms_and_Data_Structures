import timeit
import quick_sort
import random
import matplotlib.pyplot as plt
import os
import sys
import shell_sort

print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)

os.chdir(os.path.dirname(__file__))

def compare_pivot():

    fig, ax = plt.subplots()

    # pivot-->median of three
    t1 = timeit.Timer("quick_sort.qsort(x, 0, len(x)-1)", "from __main__ import quick_sort, x")

    # pivot-->start
    t2 = timeit.Timer("quick_sort.quick_sort(x, 0, len(x)-1)", "from __main__ import quick_sort, x")


    x_axis = []
    y_axis = []
    for i in range(100, 501, 100):
        x = [random.randint(1, 1000000) for i in range(i)]
        y = t1.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='blue')

    x_axis = []
    y_axis = []
    for i in range(100, 501, 100):
        x = [random.randint(1, 1000000) for i in range(i)]
        y = t2.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='red')


    plt.savefig('test.png')


def qsort_improve():
    # import quick_sort
    fig, ax = plt.subplots()
    # pivot-->median of three

    t1 = timeit.Timer("quick_sort.qsort(x, 0, len(x)-1)", globals=globals())

    # pivot-->start
    t2 = timeit.Timer("quick_sort.qsort_insert(x, 300)", globals=globals())


    x_axis = []
    y_axis = []
    for i in range(100, 501, 100):
        x = [random.randint(1, 1000000) for i in range(i)]
        globals()['x'] = x
        y = t1.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='blue')

    x_axis = []
    y_axis = []
    for i in range(100, 501, 100):
        x = [random.randint(1, 1000000) for i in range(i)]
        globals()['x'] = x
        y = t2.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='red')

    plt.savefig('test.png')

# qsort_improve()

def shell_performance():
    # import quick_sort
    fig, ax = plt.subplots()
    # pivot-->median of three

    t1 = timeit.Timer("shell_sort.shell_sort(x, 4)", globals=globals())

    # the total time is least
    t2 = timeit.Timer("shell_sort.shell_sort(x, 11)", globals=globals())
    t3 = timeit.Timer("shell_sort.shell_sort(x, 23)", globals=globals())

    x_axis = []
    y_axis = []
    for i in range(1000, 8001, 1000):
        x = [random.randint(1, 1000000) for i in range(i)]
        globals()['x'] = x
        y = t1.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='blue')

    x_axis = []
    y_axis = []
    for i in range(1000, 8001, 1000):
        x = [random.randint(1, 1000000) for i in range(i)]
        globals()['x'] = x
        y = t2.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='red')


    x_axis = []
    y_axis = []
    for i in range(1000, 8001, 1000):
        x = [random.randint(1, 1000000) for i in range(i)]
        globals()['x'] = x
        y = t3.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='green')

    plt.savefig('test.png')



if __name__ == "__main__":
    shell_performance()