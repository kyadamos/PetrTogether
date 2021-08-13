"""
petrtogether.py

    if you ever have to assign a large group of people to do different some tasks, and you happen to have some quantifiable information on a spreadsheet about:
    
        a) what tasks they usually like
        b) what they're good at
        c) what they want to learn more about
        d) how long it will take them to do something
        e) how far away they live from the place
        f) how many hours they'll probably spend doing it
        g) how much it will cost for that person to do it
        h) how much you stand to gain if that person does it
        i-z) whatever else you feel is relevant to deciding what to assign to who
    
    then hopefully this could help you. i'm not a super great programmer, but it's definitely one of the more fun and fulfilling projects i've been working on; if you have any tips or any questions, shoot me an email or a dm :)



        kyle

        kyle@adamos.systems
"""

import numpy as np
from pathlib import Path as p
import os
from match_info.Miscellaneous.dicts import get_dir_path, get_csv_path

    

def extract_data(folder,file_name,lower,upper):
    """
    Transfers data from a file to an ndarray

    Paramters :	
        
        folder : `str`, list of `str`, `pathlib.Path`
            File path location for the `PurePath` subclass, using the `join` function

        file_name : `str`, `pathlib.Path`
            File name for the same thing that I said the folder was for. Can be a .csv or .txt file, but you have to edit your file if you're not using commas to separate your data. That'll be `delimeter`

        
        lower, upper : `int`
            Column numbers to read from .csv. Mine were in the back of the files, so hopefully yours are too. If not, you can split it yourself, too. It cuts off the headers and turns everything into floats

    Returns	: ndarray
            Can use it for pulling out student preferences, project team capacities, etc. for building weight matrices and constraints
    """

    csv_data = np.genfromtxt(
        fname=p(os.path.join(folder,file_name)),
        dtype=float,
        delimiter=','
        ,skip_header=1,
        usecols=range(lower,upper)
    )
    
    return csv_data

# create new array without nan by either:

# creating a new array without them,
# csv_data = _csv_data[np.logical_not(np.isnan(_csv_data))]

# or setting them to 0 lol
# csv_data[np.isnan(csv_data)] = 0.

def test_create_projects(quarter,lo_constraint,up_constraint):

    # identify student preferences
    preferences = extract_data(RESPONSES_PATH,quarter,17,22)
    
    preferences[np.isnan(preferences)] = 0.
    #preferences = np.trim_zeros(np.all(preferences)) # fuck me
    preferences = np.array((preferences),dtype=int)
    total_students = np.count_nonzero(np.transpose(preferences)[1],axis=0)
    
    # determine constraints: project capacities
    project_sizes = extract_data(CONSTRAINTS_PATH,'team_size_constraints.csv',lo_constraint,up_constraint)

    project_sizes[np.isnan(project_sizes)] = 0.
    project_sizes = np.array(np.trim_zeros(project_sizes),dtype=int)
    total_projects = np.count_nonzero(project_sizes)

    print(f"\nthere are {total_students} students and {total_projects} projects\n")

    return preferences, project_sizes


if __name__ == "__main__":
    
    try:
        petr_paths = (DIR_PATH, RESPONSES_PATH, CONSTRAINTS_PATH)
        print("petr_paths updated")
        
    except NameError:
        DIR_PATH = get_dir_path(__file__)
        RESPONSES_PATH, CONSTRAINTS_PATH = get_csv_path(DIR_PATH)
        petr_paths = (DIR_PATH,RESPONSES_PATH,CONSTRAINTS_PATH)    

    if matching_quarter == "Winter":
        qtr, c_lo, c_hi = 'W21_data.csv', 2, 3
    elif matching_quarter == "Fall":
        qtr, c_lo, c_hi = 'F20_data.csv', 1, 2
        
    matching_params = [qtr,c_lo,c_hi]
    print(matching_params[i] for i in matching_params)

    preferences, project_sizes = test_create_projects(
        matching_params[0],
        matching_params[1],
        matching_params[2]
    )

    print("PREFERENCES:\n", preferences, "\n\nPROJECT SIZES:\n", project_sizes)
    