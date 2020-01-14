import timeit
import sequential_search
import binary_search
import hash_table
import random
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

def seq_bin():
    fig, ax = plt.subplots()

    t1 = timeit.Timer("sequential_search.sequential_search(x, x[random.randint(0, 10000-1)])", "from __main__ import sequential_search, x, random")
    t2 = timeit.Timer("binary_search.iter_bin_search(x, x[random.randint(0, 10000-1)])", "from __main__ import binary_search, x, random")
    t3 = timeit.Timer("binary_search.rec_bin_search(x, x[random.randint(0, 10000-1)], 0, len(x)-1, 0)", "from __main__ import binary_search, x, random")



    x_axis = []
    y_axis = []
    for i in range(10000, 200001, 10000):
        x = [random.randint(1, 1000000) for i in range(i)]
        y = t1.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='blue')

    x_axis = []
    y_axis = []
    for i in range(10000, 200001, 10000):
        x = [random.randint(1, 1000000) for i in range(i)]
        y = t2.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='red')


    x_axis = []
    y_axis = []
    for i in range(10000, 200001, 10000):
        x = [random.randint(1, 1000000) for i in range(i)]
        y = t3.timeit(number=100)
        x_axis.append(i)
        y_axis.append(y)
    ax.scatter(x_axis, y_axis, c='green')


    plt.savefig('test.png')


def hash_perform():
    fig, ax = plt.subplots()
    t1 = timeit.Timer("hash_table.rehash_func(table, x)", globals=globals())
    table_size = 101
    for load in [0.1, 0.25, 0.5, 0.75, 0.9, 0.99]:
        fill_size = int(table_size*load)

        x_axis = []
        y_axis = []
        for i in range(50000, 100001, 10000):
            table = [None] * table_size
            for m in range(fill_size):
                t = random.randint(0, 5000)
                index = hash_table.rehash_func(table, t)
                table[index] = t

            globals()['table'] = table

            globals()['x'] = random.randint(0, 5000)
            y = t1.timeit(number=i)
            x_axis.append(i)
            y_axis.append(y)
        ax.scatter(x_axis, y_axis, label=load)

        
    ax.legend()
    plt.savefig('test.png')

hash_perform()