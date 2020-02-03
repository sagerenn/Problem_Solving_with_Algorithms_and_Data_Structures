from graph import Graph
import sys
import os
import math
sys.path.append(os.path.abspath('./Chapter07'))
from binary_heap import BinHeap

def shortest_path(g, start_point):
    min_heap = BinHeap()
    start_vertex = g.get_vertex(start_point)
    start_vertex.set_distance(0)

    # set the distance of all vertices to infinite number
    for v in g:
        if v != start_vertex:
            v.set_distance(math.inf)


    min_heap.build_heap([(v.get_distance(), v) for v in g])

    # every time get a shortest vertex based on known short steps and set the distance and predecessor of its related vertices
    # O((E+V)*log(V))
    while min_heap.get_size() > 0:

        # O(log(V))
        short_vertex = min_heap.del_min()[1]

        # O(E*log(V))
        for v in short_vertex.get_connections():
            temp = short_vertex.get_distance() + short_vertex.get_weight(v)
            if v.get_distance() > temp:
                # O(log(V))
                min_heap.decrease_element( (v.get_distance(), v), (temp, v) )
                v.set_distance( temp )
                # because the connection to one vertex is many, we will need to check whether the vertex is in the heap and replace the value, that will take O(V)
                # min_heap.insert((v.get_distance(), v))
                v.set_predecessor(short_vertex)

    