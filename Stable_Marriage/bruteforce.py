# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 18:50:35 2018

@author: Mohammad Doosti Lakhani
"""

from utils import random_prefs_generator 
import random

num_of_residents = 3
num_of_hospitals = 2
capacities = 1


def brute_force(num_of_residents, num_of_hospitals, groundtruth):
    capacities = 1 # hardcoded capacity (other size need none random operations, so time is not random)
    random_matched_dict = {} # the dicitionary matched using random operations
    res_pref, hos_pref, cap = random_prefs_generator(num_of_residents, num_of_hospitals, capacities) # the preferences
    #matched_dict = extended_gale_shapley(hos_pref, res_pref, cap)    # the groundtruth
    #this loop do random things and generate different answers until it finds the stable one.
    while random_matched_dict != groundtruth:
        random_residents = random.sample(range(0,num_of_residents), num_of_hospitals)
        for idx,h in enumerate(hos_pref.keys()):
                random_matched_dict[h] = [random_residents[idx]]