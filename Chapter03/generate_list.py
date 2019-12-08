def test1(n):
    l = []
    for i in range(n):
        l = l + [i]

def test2(n):
    l = []
    for i in range(n):
        l.append(i)

def test3(n):
    l = [i for i in range(n)]

def test4(n):
    l = list(range(n))

from timeit import Timer

t1 = Timer("test1(10000)", "from __main__ import test1")
t2 = Timer("test2(10000)", "from __main__ import test2")
t3 = Timer("test3(10000)", "from __main__ import test3")
t4 = Timer("test4(10000)", "from __main__ import test4")
# print("concat " , t1.timeit(number=100))
print("append " , t2.timeit(number=1000))
print("comprehension " , t3.timeit(number=1000))
print("list range " , t4.timeit(number=1000))

