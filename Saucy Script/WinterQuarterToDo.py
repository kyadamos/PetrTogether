# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 19:49:04 2021

@author: Shashwat Sparsh
"""


'''
To Do:

Create Second Preference Swap:
    1. Take Person and check second Preference 
    2. Get Second Preference Size:
        a. if size = max, return null/break
        b. if size < max, proceed
    3. Add Student to Roster 2
    4. Remove Student from Roster 1

Create Affinity Coefficient Matrix:
    1. Estimate Project preferences for each attribute
    2. Determine affinity scores for each student

Final Application Concept:
    1. Sort Students into their primary preference.
    2. Get each student affinity score for their preferences.
    3. For each student in overflow for each project, resort them into their highest affinity projects
    4. Loop above process until sort is even: set max loop count based on trials
    5. Create Excel/Table with generated rosters

'''    