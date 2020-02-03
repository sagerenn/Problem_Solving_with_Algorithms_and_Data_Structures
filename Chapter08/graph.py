from vertex import Vertex
import sys
import os
sys.path.append(os.path.abspath('./Chapter04'))
from queue_adt import Queue

# the inplement of adjacency list to keep all the vertices and its key
class Graph():

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0
        self.num_edges = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)

        self.vert_list[f].add_neighbor(self.vert_list[t], weight)
        self.num_edges += 1

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


def bfs(s_graph, start):
    start_node = s_graph.get_vertex(start)
    if not start_node:
        raise KeyError(start + "Not found!")
    start_node.set_predecessor(None)
    start_node.set_color('gray')

    task_list = Queue()
    task_list.enqueue(start_node)

    while task_list.size() > 0:

        # O(V)
        current_node = task_list.dequeue()
        for vertex in current_node.get_connections():
            # O(E)
            if not vertex.get_color():
                vertex.set_predecessor(current_node)
                vertex.set_color('gray')
                vertex.set_distance(current_node.get_distance() + 1)
                task_list.enqueue(vertex)
        current_node.set_color('black')

def bfs_path(s_graph, end):
    end_node = s_graph.get_vertex(end)
    while end_node.get_predecessor() != None:
        print(end_node.get_key())
        end_node = end_node.get_predecessor()
    print(end_node.get_key())

# O(V^3)
def all_bfs(s_graph):
    result = {}
    for v in s_graph:
        result[v] = {}
    for i in s_graph:
        for v in s_graph:
            v.set_predecessor(None)
            v.set_color('white')

        bfs(s_graph, i.get_key())

        for v in s_graph:
            temp = []
            temp_v = v
            while temp_v.get_predecessor() != None:
                temp.append(temp_v)
                temp_v = temp_v.get_predecessor()
            result[i][v] = temp

    return result

class DFSGraph(Graph):

    def __init__(self):
        super().__init__()
        self.time = 0
        self.topological_sort_list = []
        self.component = {}

    def dfs(self, iter_list=False):
        self.time = 0
        for a_vertex in self:
            a_vertex.set_color('white')
            a_vertex.set_predecessor(None)
        if iter_list:
            temp = iter_list
        else:
            temp = self

        for a_vertex in temp:
            if a_vertex.get_color() == 'white':
                self.component[ len(self.component)+1 ] = []
                self.dfs_visit(a_vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.set_color('gray')
        self.time += 1
        start_vertex.set_discovery(self.time)
        for a_vertex in start_vertex.get_connections():
            if a_vertex.get_color() == 'white':
                a_vertex.set_predecessor(start_vertex)
                self.dfs_visit(a_vertex)
        start_vertex.set_color('black')
        self.time += 1
        start_vertex.set_finish(self.time)
        self.topological_sort_list.append((self.time, start_vertex))
        self.component[ len(self.component) ].append(start_vertex)


    def topological_sort(self):
        if self.time == 0:
            self.dfs()
        self.topological_sort_list.sort(key=lambda x: x[0], reverse=True)
        return [ i[1] for i in self.topological_sort_list]

    def scc(self):
        to_list = self.topological_sort()
        transpose_graph = DFSGraph()
        for vertex in self:
            for adj in vertex.get_connections():
                transpose_graph.add_edge(adj, vertex)
        transpose_graph.dfs(iter_list=to_list)
        return self.component


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 2, 1)
    g.add_edge(5, 4, 8)

    for i in g:
        print(i)
        