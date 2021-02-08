import pandas as pd
import numpy as np
import cvxpy as cp
import match_info
from match_info.matchmake import Matcher

from pathlib import Path as p
import sys,os

# get the csv files in the path
csv_loc = p(os.path.dirname(__file__))
teams_csv = 'F20_data.csv' # PUT YOUR CSV OF AVAILABLE TEAMS IN HERE!!
t_path = p(os.path.join(csv_loc, 'match_info', teams_csv))

constraints_csv = 'team_size_constraints.csv'
c_path = p(os.path.join(csv_loc, 'match_info', constraints_csv))

# what teams am i matching students to
# - input: csv files of available projects (relevant columns to match by) and constraints
## constraints = team size, GPA (later)
# - output: pandas dataframe? with 

proj_col = [0,17,18,19,20,21]
cons_col = [1]
project = Matcher(t_path,proj_col,c_path,cons_col)
print(project.responses)

# what are the student's preferences
# - input: csv files of student responses, relevant columns to match by
# - output: 

# how am i matching students to teams
# - variables
## project interest
## unit load
## skills
## behavior
## role
# - objective function
# - constraints
# - solver

constraints = [
    ]

objective = cp.Minimize(cp.sum())