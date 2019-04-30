from collections import deque
from graphs.utils import random_graph_generator


def BFFunc(graph, graphRev):
    def BFS(node):
        nodeList = []
        queue = deque([])
        queue.append(node)
        node.visited = True
        nodeList.append(node)

        while (len(queue) > 0):
            graphNode = queue.popleft()
            for adj in graphNode.adjacent:
                if not adj.visited:
                    adj.visited = True
                    queue.append(adj)
                    nodeList.append(adj)
        return nodeList

    result = []

    findedNodes = []
    for i in range(len(graph)):
        if findedNodes.__contains__(graph[i]):
            continue

        nodeList = BFS(graph[i])
        nodeListRev = BFS(graphRev[i])

        temp = []
        for n in nodeList:
            for nRev in nodeListRev:
                if n.id == nRev.id:
                    temp.append(n)
                    findedNodes.append(n)
        result.append(temp)

        for node in graph:
            node.visited = False
        for node in graphRev:
            node.visited = False
    return result


n, m = random_graph_generator(10, True)
result = BFFunc(n, m)

for i in result:
    for j in i:
        print(j.id, end=" | ")
    print()
