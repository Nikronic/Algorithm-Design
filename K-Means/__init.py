# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:21:04 2018

@author: Mohammad Doosti Lakhani
"""

# import libraries
from K_means import generate_sample_data, fit, plotter
import matplotlib.pyplot as plt
import time
import numpy as np


def run(num_of_clusters=3, center_coor = [[2,2],[5,5],[8,1]], random_data_shape= (200,2)):    
    args = (num_of_clusters,center_coor,random_data_shape)
    z = generate_sample_data(*args)
    centers = fit(z,num_of_clusters)
    #plotter(z,centers)
    return z, centers, plotter
    

def check_runtime():
    n_clusters = 3
    
    center_coordinates = [
            [[2,2],[5,3],[2,1]],
            [[4,2],[1,5],[1,7]],
            [[6,3],[5,4],[2,6]],
            [[2,7],[3,5],[8,7]],
            [[3,1],[5,7],[8,2]],
            [[2,2],[7,5],[4,1]],
            [[4,9],[4,4],[8,1]],
            [[1,3],[2,1],[1,1]],
            [[8,8],[8,2],[2,5]],
            [[5,7],[7,4],[3,1]]
            ]
    
    random_data_shapes = [
            (100,2),
            (1000,2),
            (2000,2),
            (5000,2),
            (10000,2),
            (15000,2),
            (20000,2),
            (30000,2),
            (40000,2),
            (50000,2)
            ]
    
    run_times = []
    
    for i in range(len(center_coordinates)):
        start_time = time.time()
        run(n_clusters, center_coordinates[i], random_data_shapes[i])
        print("#{} training data --- {} seconds ---".format(random_data_shapes[i][0],time.time() - start_time))
        run_times.append((time.time() - start_time))
    return run_times
    
    
    
t = check_runtime()
plt.plot(np.linspace(0,50000,10),t)