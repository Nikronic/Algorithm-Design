
import numpy as np
import random
import itertools


class graph():
    def __init__(self, visited=False, id=None, adjacent=None, directed=False, color=-1, low=-1, index=-1):
        self.visited = visited
        self.id = id
        self.adjacent = adjacent if adjacent != None else []
        self.directed = directed
        self.color = color
        self.low = low
        self.index = index

    def add_adjacent(self, graph):
        self.adjacent.append(graph)
        if self.directed == False:
            graph.adjacent.append(self)

    def describe(self):
        ads = [i.id for i in self.adjacent]
        print("ID=#{}, Visited = {}, color={} ,adjacent={}".format(self.id, self.visited, self.color, ads))


def show_graph(nodes):
    print("######### START GRAPH #########")
    for n in nodes:
        print(n.describe())
    print("######### END GRAPH #########")

def get_random_pairs(numbers, directed):
    # Generate all possible non-repeating pairs
    if not directed:
        pairs = list(itertools.combinations(numbers, 2))
    else:
        pairs = list(itertools.permutations(numbers, 2))

    # Randomly shuffle these pairs
    random.shuffle(pairs)
    if not directed:
        indx = (np.random.rand(len(pairs)) > 0.5) * 1
    else:
        indx = (np.random.rand(len(pairs)) > 0.85) * 1
    tuples = []
    for idx, f in enumerate(indx):
        if f == 1:
            tuples.append(pairs[idx])
        else:
            pass
    return tuples


def random_graph_generator(nodes, directed=False,return_edges=False):
    """
  Args:
    nodes: number of graphs
    max_nodes: maximum number of nodes in each graph
    directed: directed graph or undirected graph
  """
    edges = get_random_pairs(list(range(nodes)),directed)
    graph_nodes = []  # list of nodes of graph
    reverse_graph_nodes = [] # list of nodes of reversed graph in directed mode
    for i in range(nodes):
        graph_nodes.append(graph(id=i + 1, directed=directed))
        if directed:
            reverse_graph_nodes.append(graph(id=i + 1, directed=directed))

    for e in edges:
        s_index = e[0]
        t_index = e[1]
        graph_nodes[s_index].add_adjacent(graph_nodes[t_index])

        if directed:
            rs_index = e[1]
            rt_index = e[0]
            reverse_graph_nodes[rs_index].add_adjacent(reverse_graph_nodes[rt_index])

    if not directed:
        if return_edges:
            return graph_nodes, len(edges)
        else:
            return graph_nodes
    else:
        if return_edges:
            return graph_nodes, reverse_graph_nodes, len(edges)
        else:
            return graph_nodes, reverse_graph_nodes


# usage
# g,gr =random_graph_generator(10,directed=True)


