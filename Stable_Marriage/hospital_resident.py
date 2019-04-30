# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:00:58 2018

@author: Mohammad Doosti Lakhani
"""

# import utils library which contains some preprocessing and postprocessing functions
from utils import worst_resident_index, free_residents, has_bad_member, random_prefs_generator, check_inputs

def extended_gale_shapley(hospital_prefs_dict, resident_prefs_dict, capacities):
    """
    Main algorithm of extend version of Gale-Shapley algorithm for resident-hospital problem
    """
    
    check_inputs(hospital_prefs, resident_prefs)
    # building a empty list for every hospital in dictionary.
    matched_dict = {hosp: [] for hosp in hospital_prefs_dict}
    free_residents_list = free_residents(resident_prefs_dict, matched_dict)
    while free_residents_list:
        # match first prefrence items
        resident = free_residents_list[0]
        hospital = resident_prefs_dict[resident][0]
        matched_dict[hospital].append(resident)
        
        if has_bad_member(hospital, matched_dict, capacities):
            worst_resident = hospital_prefs_dict[hospital][worst_resident_index(hospital, hospital_prefs_dict, matched_dict)]
            matched_dict[hospital].remove(worst_resident)
            
        if not has_bad_member(hospital, matched_dict, capacities):
            worst_idx = worst_resident_index(hospital, hospital_prefs_dict, matched_dict)
            successors = hospital_prefs_dict[hospital][worst_idx + 1:]

            if successors:
                for resident in successors:
                    hospital_prefs_dict[hospital].remove(resident)
                    if hospital in resident_prefs_dict[resident]:
                        resident_prefs_dict[resident].remove(hospital)
        free_residents_list = free_residents(resident_prefs_dict, matched_dict)
        
    return matched_dict
        

# Example for trace:
# =============================================================================
# resident_prefs = {'1': ['2'],
#                   '7': ['2', '5'],
#                   '6': ['2', '4', '5'],
#                   '8': ['5', '2', '4'],
#                   '3': ['2', '5', '4']}
# hospital_prefs = {'5': ['3', '6', '7','8'],
#                   '2': ['3', '1', '7', '8', '6'],
#                   '4': ['3', '1', '6','8']}
# capacities = {h: 2 for h in hospital_prefs.keys()}
# =============================================================================

resident_prefs, hospital_prefs, capacities = random_prefs_generator(5,3,1)
matching = extended_gale_shapley(hospital_prefs, resident_prefs, capacities)
matching
