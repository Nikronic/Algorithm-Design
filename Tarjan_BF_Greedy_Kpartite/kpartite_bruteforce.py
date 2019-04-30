
from itertools import combinations
from graphs.utils import random_graph_generator


nodes = random_graph_generator(10)




def bf(nodes):
    comList = []
    for i in reversed(range(len(nodes))):
        com = list(combinations(nodes, i + 1))
        comList.append(com)

    for item in comList:
        for subList in item:
            failed = False
            com2 = combinations(subList, 2)
            for k in com2:
                if k[0].adjacent.__contains__(k[1]):
                    failed = True
                    break
            if not failed:
                return subList
    return None


result = bf(nodes)

if result:
    for i in result:
        print(i.id, "", end='')
