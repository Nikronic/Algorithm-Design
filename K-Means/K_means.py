# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 09:21:04 2018

@author: Mohammad Doosti Lakhani
"""


# import libraries
import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

def generate_sample_data(n_clusters, center_coordinates, random_data_shape):
    
    # the coordinate of new random data
    # we will build random data around this centers
    cc = np.zeros(shape = (n_clusters,2)) 
    for i in range(len(cc)):
        cc[i] = np.array(center_coordinates[i])
            
    # data points to cluster       
    data = np.zeros(shape=(n_clusters, random_data_shape[0],random_data_shape[1]))
    
    for i in range(len(cc)):
        data[i] = np.random.randn(*random_data_shape) + cc[i]
        
    data = data.reshape((n_clusters*random_data_shape[0], random_data_shape[1]))
    return data


def plotter(data, centers = []):
    # only work for 2 dimensional data
    plot = plt.scatter(data[:,0], data[:,1], s = 4)
    if len(centers) != 0:
        plot = plt.scatter(centers[:,0], centers[:,1], marker='d', c='red', s=70)
    return plot


def fit(data, n_clusters, max_iterations = 300, threshold = 1e-10):
    m = data.shape[0] # number of training data
    n = data.shape[1] # number of features of every single train data
    
    # we generate random centers
    # we use standard deviation and mean to ensure centers cover all data and distributed normally
    mean = np.mean(data, axis = 0) # mean of each feature
    sigma = np.std(data, axis = 0) # standard deviation of each feature
    
    # randomly selected centers
    centers = np.random.randn(n_clusters,n)*sigma + mean
    
    
    old_centers = np.zeros(centers.shape) # save old centers to capture error in every update
    new_centers = deepcopy(centers) # update each time with new mean and std
    distances = np.zeros((m,n_clusters)) # distances of each point to the all centeres
    
    e = np.linalg.norm(new_centers - old_centers) # metric function = sqrt(sum((a-b)**2))
    threshold = 1e-10 # when we updating centers, if error was less than this, we finish our job
    
    while  max_iterations > 0 and e > threshold:
        for i in range(n_clusters):
            # measure distance to each center
            distances[:,i] = np.linalg.norm(data - centers[i], axis = 1)
        
        # assign clusters to the closest center            
        clusters = np.argmin(distances, axis = 1)    
        old_centers = deepcopy(new_centers)
    
        # update centers
        for i in range(n_clusters):
            new_centers[i] = np.mean(data[clusters == i], axis = 0)
        
        e = np.linalg.norm(new_centers - old_centers)
        max_iterations -= max_iterations-1
        
    return new_centers


d = generate_sample_data(2, [[5,7],[7,4],[3,1]], (1000,2))
c = fit(d, 2)
p = plotter(d,c)
p
