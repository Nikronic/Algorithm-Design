
from graphs.utils import random_graph_generator

nodes, reverse = random_graph_generator(5, directed=True)


def tarjanFunc(graph):
    stack = []
    stackCount = 0
    result = []

    def Dfs(node, stackCount):
        stack.append(node)
        node.index = stackCount
        node.low = stackCount
        stackCount = stackCount + 1

        for nodeAdjacent in node.adjacent:
            if nodeAdjacent.index == -1:
                Dfs(nodeAdjacent, stackCount)
                node.low = min(node.low, nodeAdjacent.low)
            elif stack.__contains__(nodeAdjacent):
                node.low = min(node.low, nodeAdjacent.low)

        if node.low == node.index:
            top = stack.pop()
            temp = [top]
            while top != node:
                top = stack.pop()
                temp.append(top)
            result.append(temp)

    for node in graph:
        if node.index == -1:
            Dfs(node, stackCount)

    return result


result = tarjanFunc(nodes)

for i in nodes:
    print(i.describe())

for i in result:
    for j in i:
        print(j.id, end=" | ")
    print()
