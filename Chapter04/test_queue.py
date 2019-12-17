import test
from queue_adt import Queue, ConstantQueue
from timeit import Timer
import random

def test_operations():
    q = Queue()
    q.enqueue(3)
    print(q)
    q.enqueue('dog')
    q.enqueue(True)
    q.enqueue(['sd'])
    print(q)
    print(q.dequeue())
    print(q)
    print(q.is_empty())
    print(q.size())


# test_operations()


def host_potato(people_list, max):
    q = Queue()
    for p in people_list:
        q.enqueue(p)
    while q.size() > 1:
        num = random.randint(1, max)
        # use the fix position to record the eliminated people, pass num people through it
        for i in range(num):

            # make a circle, move the people rather than the item
            q.enqueue(q.dequeue())
        q.dequeue()
    return q.dequeue()

print(host_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))


# def time_performance():
# q = Queue()
# q = ConstantQueue()
# t = Timer("q.enqueue(5)", "from __main__ import q")
# x = t.timeit(number=500000)
# t = Timer("q.dequeue()", "from __main__ import q")
# y = t.timeit(number=500000)
# print(x,y)

