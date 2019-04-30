
from graphs.utils import random_graph_generator
from itertools import combinations
from copy import deepcopy

nodes = random_graph_generator(7)


# Algorithms
def min_kpartite(nodes, max_indep_set_size=None):
    graph = deepcopy(nodes)
    p_graphs = list(combinations(graph, len(nodes)))
    max_greedy = -1
    mis = None
    for i, graph in enumerate(p_graphs):
        graph_greedy, max_greedy_new = first_fit(graph)
        if max_indep_set_size:
            if max_greedy_new >= max_indep_set_size:
                mis = graph_greedy
                max_greedy = max_greedy_new
                break
        else:
            if max_greedy_new >= max_greedy:
                max_greedy = max_greedy_new
                mis = graph_greedy
    return mis, max_greedy


def first_fit(nodes):
    graph = deepcopy(nodes)
    available_color = len(graph) * [True]

    graph[0].color = 0
    for i, node in enumerate(graph[1:]):
        for ad in node.adjacent:
            if ad.color != -1:
                available_color[ad.color] = False
        ic = next(idx for idx, c in enumerate(available_color) if c == True)
        node.color = ic
        available_color = len(graph) * [True]
    colors = [n.color for n in graph]
    max_size = max([colors.count(i) for i in set(colors)])
    return graph, max_size


def show_result(nodes, max_size):
    print('Graph with #{} nodes has maximum independent set of size #{}\n'.format(len(nodes), max_size))
    for n in nodes:
        print("ID=", n.id, ", color=", n.color)


show_result(*min_kpartite(nodes))
