from graph import Graph, bfs, bfs_path

def build_graph(missionaries, cannibals):
    g = Graph()
    all_vertices = []
    for m in range(missionaries+1):
        for c in range(cannibals+1):
            over_m = missionaries - m
            over_c = missionaries - c
            if ( ( over_m > 0 and over_m >= over_c) or over_m == 0) and \
            ( (m > 0 and m >= c) or m == 0 ):
                for t in [-1, 1]:
                    all_vertices.append([m, c, over_m, over_c, t])

    for i in all_vertices:
        for j in all_vertices:
            if i != j:
                temp = (i[0] + i[1]) - (j[0] + j[1])
                temp1 = i[0] - j[0]
                temp2 = i[1] - j[1]
                # temp3 = (i[2] + i[3]) - (j[2] + j[3])
                if temp > 0 and temp1 >= 0 and temp2 >= 0:
                    if temp <= 2 and temp1 <= 2 and temp2 <= 2 and j[4] == 1 and i[4] == -1:
                    # if temp <= 2:
                        g.add_edge(str(i), str(j))
                elif temp < 0 and temp1 <= 0 and temp2 <= 0:
                    if temp >= -2 and temp1 <= 2 and temp2 <= 2 and j[4] == -1 and i[4] == 1:
                    # if temp >= -2:
                        g.add_edge(str(i), str(j))

    return g


if __name__ == "__main__":
    river_graph = build_graph(3,3)
    bfs(river_graph, str([3, 3, 0, 0, -1]))
    bfs_path(river_graph, str([0, 0, 3, 3, 1]))

