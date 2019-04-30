
from graphs.utils import random_graph_generator
nodes = random_graph_generator(5)


def connected_parts(nodes):
    for node in nodes:
        if node.visited == False:
            dfs(node)
            print()


def dfs(node):
    node.visited = True
    print(node.id, end='')
    for adj in node.adjacent:
        if not adj.visited:
            dfs(adj)

connected_parts(nodes)

