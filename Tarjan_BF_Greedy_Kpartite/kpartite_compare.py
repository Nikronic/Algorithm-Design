from graphs.utils import show_graph, random_graph_generator
from graphs.kpartite import min_kpartite
from graphs.kpartite_bruteforce import bf
import matplotlib.pyplot as plt
import timeit
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#graph_sizes = [5,6,7,8,9,10,11,12,13,14,15,20,25,35,50,75,100,150,200,400,600,1000]
#graph_sizes = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
graph_sizes = [5,6,7,8,9,10,11]
bf_time = []
greedy_time = []
edges_sizes = []
for i in range(len(graph_sizes)):
    graph_, reversed_graph_, edges_count = random_graph_generator(graph_sizes[i], directed=True, return_edges=True)
    edges_sizes.append(edges_count)

    start_time = timeit.default_timer()
    res_bf = bf(graph_)
    max_independent_set_size = len(res_bf)
    bf_time.append((timeit.default_timer() - start_time))

    start_time = timeit.default_timer()
    res_greedy, miss = min_kpartite(graph_, max_independent_set_size)
    greedy_time.append((timeit.default_timer() - start_time))



fig = plt.figure()
ax = Axes3D(fig)
ax.plot(xs=np.linspace(edges_sizes[0],edges_sizes[len(edges_sizes)-1],len(edges_sizes)), ys=graph_sizes, zs=bf_time, color='red', label ='BF', linestyle='--')
ax.plot(xs=np.linspace(edges_sizes[0],edges_sizes[len(edges_sizes)-1],len(edges_sizes)), ys=graph_sizes, zs=greedy_time, color='blue', label ='Greedy')
ax.legend()
plt.show()
