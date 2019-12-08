comparing different programs that solve the same problem, which is best?
The answer is cost
1. time and resource of running, the complexity of data structure and algorithm
2. the time of other people understanding, readable name, comment, explicitly state
3. the time of maintain --> refactor, object-oriented programming, bug free, include all edge cases
4. the potential value of sercurity

the algorithm can simplify the repeat computation to one step or more quick way, that is the math.

execution time 
1. benchmark analysis, trak the actual time required for 'the same program', the physisc env, maybe it's suitable for large program, which can show the grap clearly. It relies on the context which doesn't belongs to the algorithm
2. Big-O Notation, using the amount(m+ny) of assignment steps to express the time, one simple operation is the smallest time(x) of computer, the total time will be ( (m + ny) * x). The n is size of the problem. 
    a. when n (x-axis) get larger, the time will be larger
    b. when the n(input numnbers) is fix, the order of magnitude: 2^n >> n^3 >> n^2 >> N log N >> n >> log N >> 1
    c. the dominant part is the most significant
    d. from kinds of input data set, the performance can be devided to worse, average, best
    e. In most situation, the average case is common. if not, maybe need to consider the another solution.


# List

The designer will focus on optimizing the common operations.
1. indexing, independent of the size of the list, O(1). In memory, the python will remember the memory location(x) of beginning index, the memory location of other indexes can be calculated by x + (index)
2. assignment, independent of the size of the list, O(1)
3. append, O(1)
4. concatenation, O(k), the length of the list that is being concatenated
5. pop(), O(1)
6. pop(i), O(n), when an item takes away from the list, others will be shifted to the closer to the beginning.
7. insert(i, item), O(n)
8. del, O(n)
9. iteration, O(n)
10. contains(in), O(n)
11. get slice[x:y], O(k)
12. del slice, O(n)
13. set slice, O(n+k)
14. reverse, O(n)
15. sort, O(n log n)
16. multiply, O(nk)

using the `timeit` module to measure the time by running functions in a consistent environment and using the timing mechanisms that are as similar as possible across operation systems. return the seconds of the total amount of test, the default is 1,000,000.

# dictionary

average performance
1. copy, O(n)
2. get item, O(1)
3. set item, O(1)
4. delete item, O(1)
5. contains(in), O(1)
6. iteration, O(n)
