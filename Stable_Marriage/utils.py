# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:12:48 2018

@author: Mohammad Doosti Lakhani
"""


import numpy as np
import random

def free_residents(residents_prefs_dict, matched_dict):
    """
    In this function, we return a list of resident who do not have empty prefrences list and unmatched with any hospital.
    """
    
    fr = []
    for res in residents_prefs_dict:
        if residents_prefs_dict[res]:
            if not (any(res in match for match in matched_dict.values())):
                fr.append(res)
    return fr

def worst_resident_index(hospital, hospital_prefs_dict, matched_dict):
    """
    returns the index of worst resident assigned to the hospital based on hospital's prefrences list.
    """
    
    idxs = []
    for res in hospital_prefs_dict[hospital]:
        if res in matched_dict[hospital]:
            idxs.append(hospital_prefs_dict[hospital].index(res))
    return max(idxs)
    
    


def has_bad_member(hospital, matched_dict, capacities):
    """
    We check if currently hospital has more residents than it's capacity, so we have to remove worst resident based on this criteria.
    """
    
    if len(matched_dict[hospital]) > capacities[hospital]:
        return True
    elif len(matched_dict[hospital]) == capacities[hospital]:
        return False
    else: 
        return False
    
    return False

def random_prefs_generator(num_of_residents, num_of_hospitals, capacities_size):
    """
    In this function we generates 2 dictionay of residents and hospitals and theirs prefrences.
    
    Example:
        
    resident_prefs = {'A': ['C'],
                 'S': ['C', 'M'],
                 'J': ['C', 'G', 'M'],
                 'L': ['M', 'C', 'G'],
                 'D': ['C', 'M', 'G']}
    hospital_prefs = {'M': ['D', 'J', 'S', 'L'],
                 'C': ['D', 'A', 'S', 'L', 'J'],
                 'G': ['D', 'A', 'J', 'L']}
    """

    
    residents_prefs = {}
    hospitals_prefs = {}
    
    num_of_hospitals += num_of_residents
    # we create prefrences list with these sizes
    res_random_sizes = np.random.randint(low= 1, high=num_of_residents+1, size=abs(num_of_hospitals-num_of_residents)+1)
    hos_random_sizes = np.random.randint(low= 1, high=abs(num_of_hospitals-num_of_residents)+1, size=num_of_residents)
    
    # fill random from size of residents and hospitals
    for i in range(num_of_residents):
        residents_prefs[i] = random.sample(range(num_of_residents,num_of_hospitals), hos_random_sizes[i])
    for i in range(abs(num_of_hospitals-num_of_residents)):
        hospitals_prefs[i+num_of_residents] = random.sample(range(num_of_residents), res_random_sizes[i])
    
    for resident in residents_prefs.keys():
        for hospital in residents_prefs[resident]:
            if resident not in hospitals_prefs[hospital]:
                hospitals_prefs[hospital].append(resident)
    
    capacities = {h: capacities_size for h in hospitals_prefs.keys()}
    
    return residents_prefs, hospitals_prefs, capacities


def check_inputs(hospital_prefs_dict, resident_prefs_dict):
    for resident in resident_prefs_dict.keys():
        for hospital in resident_prefs_dict[resident]:
            if resident not in hospital_prefs_dict[hospital]:
                raise ValueError( 'Hospitals must rank all residents who rank them.')