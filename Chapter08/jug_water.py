from graph import Graph, bfs, bfs_path


# just cover some vertices of graph
def remain_water(jug1, jug2, target, jug1_remain, jug2_remain, temp):
    if jug1_remain == target or jug1_remain == target:
        return True
    elif jug1_remain > jug1:
        return False
    elif jug2_remain > jug2:
        return False
    elif (jug1, jug2, jug1_remain, jug2_remain) in temp:
        return False
    else:
        temp.append((jug1, jug2, jug1_remain, jug2_remain))

        # some edges in graph
        found = remain_water(jug1, jug2, target, jug1, jug2_remain, temp) or \
            remain_water(jug1, jug2, target, jug1_remain, jug2, temp) or \
                remain_water(jug1, jug2, target, min(jug1, jug1_remain + jug2_remain), max(0, jug2_remain-(jug1-jug1_remain)), temp) or \
                remain_water(jug1, jug2, target, max(0,jug1_remain-(jug2-jug2_remain)), min(jug2, jug1_remain + jug2_remain), temp) or \
                    remain_water(jug1, jug2, target, jug1_remain, 0, temp) or \
                    remain_water(jug1, jug2, target, 0, jug2_remain, temp)

        if found:

            # vertex 
            print(jug1, jug2, jug1_remain, jug2_remain)
            return found


# we can build a graph with all state of jugs as vertices, and the action as edge, and use BFS to find the shortest path without check the condition we don't need to

def build_graph(jug1, jug2, jug1_remain, jug2_remain):
    g = Graph()
    all_states = []
    for i in range(jug1+1):
        for j in range(jug2+1):
            all_states.append( [jug1, jug2, i, j] )

    for i in all_states:
        for j in all_states:
            if i != j:
                if (j[2] == jug1 and i[3] == j[3]) or \
                (j[3] == jug2 and i[2] == j[2]) or \
                (j[3] == 0 and i[2] == j[2]) or \
                (j[2] == 0 and i[3] == j[3]) or \
                (j[2] == min(jug1, i[2]+i[3]) and j[3] == max(0, i[3] - ( jug1-i[2] ) )) or \
                (j[3] == min(jug2, i[2]+i[3]) and j[2] == max(0, i[2] - ( jug2-i[3] ) )):
                    g.add_edge(str(i), str(j))

    return g


if __name__ == "__main__":
    # remain_water(4, 3, 2, 0, 0, [])
    jug_graph = build_graph(4, 3, 0, 0)
    bfs(jug_graph, str([4, 3, 0, 0]))
    bfs_path(jug_graph, str([4, 3, 2, 0]))
