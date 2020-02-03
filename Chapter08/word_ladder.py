from graph import Graph, bfs
import os

def build_graph(word_list):
    g = Graph()
    d = {}

    # create budges and vertices
    # O(4|V|)
    with open(word_list, 'r') as f:
        for word in f:
            word = word.strip()
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                if d.get(pattern):
                    d[pattern].append(word)
                else:
                    d[pattern] = [word]

    # create edges
    # O(4*2|V|+|E|)
    for i in d:
        for word1 in d[i]:
            for word2 in d[i]:
                if word1 != word2:
                    g.add_edge(word1, word2)

    return g
                
if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))
    word_graph = build_graph("four_digits_words.txt")
    bfs(word_graph, 'FOOL')
    target = word_graph.get_vertex('SAGE')
    while target:
        print(target.get_key(), target.get_distance())
        target = target.get_predecessor()
