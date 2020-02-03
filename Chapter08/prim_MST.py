from graph import Graph
import sys
import os
import math
sys.path.append(os.path.abspath('./Chapter07'))
from binary_heap import BinHeap

def prim_tree(g, start):
    pq = BinHeap()

    for v in g:
        v.set_predecessor( None )
        v.set_distance( sys.maxsize )

    start.set_distance(0)

    pq.build_heap( [ (v.get_distance(), v) for v in g ] )

    while pq.get_size() > 0:

        # remove priority queue to add to MST
        current_node = pq.del_min()[1]
        for v in current_node.get_connections():
            temp = current_node.get_weight(v)
            if (v.get_distance(), v) in pq and v.get_distance() > temp:
                pq.decrease_element( (v.get_distance(), v), (temp, v) )

                v.set_distance( temp )
                v.set_predecessor( current_node )