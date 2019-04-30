# %% Import Libraries
from utils import edges, show_graph, Graph, get_input, sort_edge, is_connected
from copy import deepcopy


# %% Algorithm
def kruskal(graph):
    """
    Apply Kruskal algorithm to find minimum spanning tree of a graph

    :param graph: A list of nodes (a graph)
    :return: Spanning tree of a graph as a list of nodes (a graph)
    """

    edges = sort_edge(graph)
    graph = deepcopy(graph)
    for e in edges:
        s, d, w = e

        des_node = [n for n in graph if n.idx == d][0]
        for n in graph:
            if n.idx == s:
                n.remove_adjacent(d)
                print(s, '->',d,':',w,' Removed!')
                break
        if not is_connected(graph):
            for n in graph:
                if n.idx == s:
                    n.add_adjacent(des_node, w)
                    print(s, '->',d,':',w,' Added!')

    return graph


# %% Test
g = get_input()
g = kruskal(g)
edges(g, p=True)


# this is sample input.
# Look at the image in the root directory please.
# 0 1 4
# 0 7 8
# 1 2 8
# 1 7 11
# 2 3 7
# 2 8 2
# 7 8 7
# 7 6 1
# 8 6 6
# 6 5 2
# 2 5 4
# 3 5 14
# 3 4 9
# 5 4 10
# 0