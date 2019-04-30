class Graph:
    def __init__(self, visited=False, idx=None, adjacent=None):
        """
        Generates a single node of undirected weighted graph

        :param visited: To use for algorithms like DFS to check visited nodes
        :param idx: Just for demonstration purposes
        :param adjacent: Adjacent nodes of current node
        """
        self.visited = visited
        self.idx = idx
        self.adjacent = adjacent if adjacent is not None else []

    def add_adjacent(self, g, w):
        """
        Add a node as a adjacent of current node

        :param g: target node as adjacent
        :param w: weight of edge to node g
        :return: None
        """

        self.adjacent.append({g: w})
        g.adjacent.append({self: w})

    def remove_adjacent(self, d):
        """
        Remove a node from adjacent of current node

        :param d: Node to remove by its index value
        :return: None
        """

        len_i = len(self.adjacent)
        i = 0
        while i < len_i:
            if list(self.adjacent[i].keys())[0].idx == d:
                adj = list(self.adjacent[i].keys())[0].adjacent
                len_j = len(adj)
                j = 0
                while j < len_j:
                    if len(adj) > 0:
                        if list(adj[j].keys())[0].idx == self.idx:
                            del adj[j]
                            len_j -= 1
                        j += 1
                del self.adjacent[i]
                len_i -= 1
                break
            i += 1


    def describe(self):
        """
        Describe some of current node's features

        :return: String
        """
        ads = [list(i.keys())[0].idx for i in self.adjacent]
        print("ID=#{}, Visited = {} ,adjacent={}".format(self.idx, self.visited, ads))


def show_graph(nodes):
    """
    Print a graph by printing all nodes and their adjacent

    :param nodes: A list of nodes of a graph
    :return: None
    """
    print("######### START GRAPH #########")
    for n in nodes:
        print(n.describe())
    print("######### END GRAPH #########")


def get_input():
    """
    Get user input to build graph by getting graph size and edges with corresponding weights

    :return: A list of nodes (a graph)
    """

    print('Number of nodes')
    size = input()
    print('Input edges in this format: "src dst weight"')
    print('Enter 0 to exit.')

    graph = []
    for i in range(int(size)):
        graph.append(Graph(idx=i))

    e = input()
    while e != '0':
        es = e.split()
        src, dst, w = int(es[0]), int(es[1]), int(es[2])
        graph[src].add_adjacent(graph[dst], w)
        e = input()
    return graph


def edges(graph, p=False):
    """
    Gets a list of nodes (a graph) and show its edges with weights

    :param graph: A list of nodes
    :param p: print edges or just return the list
    :return: A list of tuple containing source, destination nodes of a edge and its weight
    """

    e = []
    for n in graph:
        for a in n.adjacent:
            if p:
                print(n.idx, ' -> ', list(a.keys())[0].idx, ', w=', a[list(a.keys())[0]])
            else:
                e.append((n.idx, list(a.keys())[0].idx, a[list(a.keys())[0]]))
    if not p:
        return e


# %% Tools
def dfs(v, graph):
    """
    DFS algorithm

    :param v: A node of graph
    :param graph: A list of nodes (A graph)
    :return: None
    """

    v.visited = True
    for a in v.adjacent:
        if not list(a.keys())[0].visited:
            dfs(list(a.keys())[0], graph)


def is_connected(graph):
    """
    Check if graph is connected or not using DFS visited nodes count

    :param graph: A list of nodes (A graph)
    :return: True if connected, False if not
    """

    dfs(graph[0], graph)
    count = 0
    for g in graph:
        if g.visited:
            count += 1
    visit_reset(graph)
    return len(graph) == count


def visit_reset(graph):
    """
    Set visited flag of all nodes in graph to False

    :param graph: A list of nodes (A graph)
    :return: None
    """
    for n in graph:
        n.visited = False


def sort_edge(graph):
    """
    Sort the edges of graph in non-increasing order

    :param graph: A list of nodes (A graph)
    :return: A list of tuple containing source, destination nodes of a edge and its weight
    """

    edge = edges(graph)
    edge.sort(key=lambda x: x[2], reverse=True)
    return edge


def clean_edges(edges):
    """
    Gets a list of 3-member tuples and remove backward edges (no need in undirected graph)

    :param edges: A list of tuples
    :return: A list of tuples with half size
    """

    e = [d for i, d in enumerate(edges) if i % 2 == 0]
    return e


def remove_redundant_edges(graph, edges):
    """

    Gets a list of nodes as a graph and a list of 3-member tuples as edges and remove edges from graph

    :param graph: A list of nodes (a graph)
    :param edges: A list of 3-member tuples in "src, des, weight" format
    :return: new graph
    """

    edges = [e for e in edges if e[0] < e[1]]
    for e in edges:
        s, d, _ = e
        for g in graph:
            if g.idx == s:
                g.remove_adjacent(d)

    return graph, edges


# %% test
# g0 = Graph(idx=0)
# g1 = Graph(idx=1)
# g2 = Graph(idx=2)
# g0.add_adjacent(g1, 5)
# g1.add_adjacent(g2, 10)
# g = [g0, g1, g2]
# show_graph(g)
# show_edges(g)

