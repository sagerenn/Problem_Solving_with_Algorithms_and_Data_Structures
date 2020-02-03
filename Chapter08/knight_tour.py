from graph import Graph
import os

def knight_graph(bdsize):
    g = Graph()
    for i in range(1, (bdsize**2)+1):
        adja_list = gen_legel_moves(i, bdsize)
        for nbr in adja_list:
            g.add_edge(i, nbr)

    return g

def gen_legel_moves(id, bdsize):
    result = []
    pos = id_to_pos(id, bdsize)
    moves = [
        (1, -2),
        (1, 2),
        (-1, -2),
        (-1, 2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
    ]

    for move in moves:
        temp = [ pos[0] + move[0], pos[1] + move[1] ]
        if in_range(temp, bdsize):
            result.append( pos_to_id(temp, bdsize) )

    return result

def in_range(pos, bdsize):
    if pos[0] > 0 and pos[0] < bdsize+1 and pos[1] > 0 and pos[1] < bdsize+1:
        return True
    else:
        return False

def id_to_pos(id, bdsize):
    row = id // bdsize + 1
    col = id % bdsize
    return [row, col]

def pos_to_id(pos, bdsize):
    return (pos[0] - 1) * bdsize + pos[1]

def dfs_once(node, end_depth, result):
    result.append(node.get_key())

    if result.index(node.get_key()) != len(result)-1:
        result.pop()
        return False
    elif len(result) == end_depth:
        return True
    else:
        for i in node.get_connections():
            if dfs_once(i, end_depth, result):

                return True
        result.pop()


def dfs_once_2(node, depth, end_depth):
    if depth == end_depth and node.get_color() != 'black':
        node.set_color('black')
        return node
    elif node.get_color() == 'black':
        return False
    else:
        node.set_color('black')
        for i in node.get_connections():
            found = dfs_once_2(i, depth+1, end_depth)
            if found:
                print(i.get_key())
                i.set_predecessor(node)
                return found
        if not found:
            node.set_color('white')


def dfs_once_3(current_node, path, current_depth, limit):
    current_node.set_color('black')
    path.append(current_node)
    if current_depth < limit:
        # nbr_list = list(current_node.get_connections())
        nbr_list = order_adja_list(current_node)
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() != 'black':
                done = dfs_once_3(nbr_list[i], path, current_depth+1, limit)
            i += 1
        if not done:
            path.pop()
            current_node.set_color('white')
    else:
        done = True
    return done

# O(k^n), k is avg branching factors
def avg_edges(g):
    sum = 0
    no = 0
    for i in g:
        sum += len(i.get_connections())
        no += 1
    return sum/no

# to generate a list of vertices that has legal avaiable moves from small to large
def order_adja_list(node):
    result_list = []
    for i in node.get_connections():
        if i.get_color() != 'black':
            c = 0
            for j in i.get_connections():
                if j.get_color() != 'black':
                    c += 1
            result_list.append((c, i))

    # the key parameter is a function generate new value list before sorting
    # lambda is a small function take any nunmer of arguements, bur can only have one expression.
    result_list.sort(key=lambda x: x[0])
    return [i[1] for i in result_list]


if __name__ == "__main__":
    chess_graph = knight_graph(8)
    print(chess_graph.num_edges)
    print(avg_edges(chess_graph))
    start_node = chess_graph.get_vertex(61)
    result = []
    # dfs_once(start_node, 64, result)
    # print(len(result), result)

    # t = dfs_once_2(start_node, 0, 63)
    # while t.get_predecessor():
    #     print(t.get_key(), end=" ")
    #     t = t.get_predecessor()
    # print()

    dfs_once_3(start_node, result, 0, 63)
    for i in result:
        print(i.get_key())