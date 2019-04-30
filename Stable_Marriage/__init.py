# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 19:44:00 2018

@author: Mohammad Doosti Lakhani
"""

from bruteforce import brute_force
from utils import random_prefs_generator 
import time
from hospital_resident import extended_gale_shapley
import matplotlib.pyplot as plt
import numpy as np

#[2,2,3,4,4,5,6,6,7]
#[3,4,5,5,6,7,7,8,8]
# parameters
num_of_residents = [3,4,5,5,6]
num_of_hospitals = [2,2,3,4,4]
capacities = 1

# timers
gsh_time = [] # galeshapley time
bruteforce_time = [] # brtute force time

for rc,hc in zip(num_of_residents,num_of_hospitals):
    res_pref, hos_pref, cap = random_prefs_generator(rc, hc, 1)
    
    start_time = time.time()
    groundtruth = extended_gale_shapley(hos_pref, res_pref,cap)
    gsh_time.append((time.time() - start_time))
    
    start_time = time.time()
    brute_force(rc, hc, groundtruth)
    bruteforce_time.append((time.time() - start_time))
    
for gsh,bf in zip(gsh_time, bruteforce_time):
    print("Gale shapley time ====>", gsh, "     Bruteforce time ====>", bf)


plt.plot(np.arange(1,6),gsh_time,color='g', label='Gale-Shapley Time')
plt.plot(np.arange(1,6),np.array(bruteforce_time)/1000,color='r' ,linestyle='dashed', label='Bruteforce Time', alpha=0.5)
plt.xlabel('Average number of residents and hospitals')
plt.ylabel('Time consume in miliseconds')
plt.legend()
plt.grid()
