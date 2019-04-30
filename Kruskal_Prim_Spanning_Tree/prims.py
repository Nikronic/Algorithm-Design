# %% Import Libraries
from utils import edges, show_graph, Graph, get_input, sort_edge, is_connected, remove_redundant_edges
from copy import deepcopy


# %% Algorithm
def prims(graph):
    """
    Apply Prims algorithm to find minimum spanning tree of a graph

    :param graph: A list of nodes (a graph)
    :return: Spanning tree of a graph as a list of nodes (a graph)
    """

    mst = []
    node = graph[0]
    node.visited = True
    mst.append(node)
    edges_list = edges([node])  # just initialize first node to start

    while len(mst) != len(graph):
        edges_list.sort(key=lambda x: x[2])
        min_edge = edges_list.pop(0)
        min_node = [n for n in graph if n.idx == min_edge[1]][0]
        if not min_node.visited:
            mst.append(min_node)
            min_node.visited = True
            edges_list.extend(edges([min_node]))

    mst, e = remove_redundant_edges(mst, edges_list)
    return mst, e


# %% Test
g = get_input()
mst, e = prims(g)
print('removed edges:', e)
