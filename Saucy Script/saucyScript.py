# -*- coding: utf-8 -*-
"""
Spyder Editor
print("hello world");

This is a temporary script file.
"""
"""
Reference Links

https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
https://datatofish.com/import-csv-file-python-using-pandas/
https://stackoverflow.com/questions/14365542/import-csv-file-as-a-pandas-dataframe
https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
https://www.google.com/search?client=firefox-b-1-d&q=how+to+loop+through+columns+of+data+frame
https://stackoverflow.com/questions/28218698/how-to-iterate-over-columns-of-pandas-dataframe-to-run-regression

"""

#Primary Sorting Function
def primarySorter(primaryPreference):
    switcher = {
            'Project 1':0,
            'Project 2':1,
            'Project 3':2,
            'Project 4':3,
            'Project 5':4,
            'Project 6':5,
            'Project 7':6,
            'Project 8':7,
            'Project 9':8,
            'Project 10':9,
            'Project 11':10,
            'Project 12':11,
            'Project 13':12,
            'Project 14':13,
            'Project 15':14,
            }
    return switcher.get(primaryPreference, "Invalid Preference")
#End
    
#Class Declarations
class Person:
    def __init__(self, name, projectPreferences):
        self.name = name
        self.projectPreferences = projectPreferences

class Project:
    def __init__(self, name, maxCount):
        self.name = name
        self. maxCount = maxCounter;
#End
   

import numpy as np;
#import tinkter as tk;
import pandas as pd

project1 = [];
project2 = [];
project3 = [];
project4 = [];
project5 = [];
project6 = [];
project7 = [];
project8 = [];
project9 = [];
project10 = [];
project11 = [];
project12 = [];
project13 = [];
project14 = [];
project15 = [];
projectList = [project1, project2, project3, project4, project5, project6, project7, project8, project9, project10, project11, project12, project13, project14, project15];

    
    
data = pd.read_csv (r'D:\Documents\GitHub\PetrTogether\Saucy Script\F20_dataModified.csv')   
df = pd.DataFrame(data, columns= ['Student number','Preference 1', 'Preference 2', 'Preference 3', 'Preference 4', 'Preference 5',])

#print(df);
#print(data);

for (index_label, row_series) in df.iterrows():
    student = row_series.values[0];
    primaryPreference = row_series.values[1];
    primaryIndex = primarySorter(primaryPreference);
    (projectList[primaryIndex]).append(student);
    #print(student);
    #print('Row Index label : ', index_label)
    #print('Row Content as Series : ', row_series.values)
print(projectList);

'''
for index in range(df.shape[1]): 
     
    print('Column Number : ', index) 
      
    # Select column by index position using iloc[] 
    columnSeriesObj = df.iloc[:, index] 
    print('Column Contents : ', columnSeriesObj.values) 
'''






#test = numpy.array([1,2]);
'''
#Declaring People as Arrays
person1 = np.array([0, 1, 2, 3, 0]);
person2 = np.array([1, 2, 0, 3, 0]);
person3 = np.array([0, 1, 0, 3, 2]);
person4 = np.array([0, 1, 2, 3, 0]);
person5 = np.array([1, 2, 3, 0, 0]);
person6 = np.array([0, 3, 2, 1, 0]);
person7 = np.array([3, 0, 2, 0, 1]);
person8 = np.array([2, 1, 0, 1, 3]);
people = np.array([person1, person2, person3, person4, person5, person6, person6, person8]);
'''

'''
#Declaring Projects as Arrays
project1 = [];
project2 = [];
project3 = [];
project4 = [];
project5 = [];
projectList = [project1, project2, project3, project4, project5];
'''

''' Debugging
print(project1);
project1.append(person1);
print(project1);
'''
'''
#Sorting
for i in people:                                                                #Looping through people array
    for j in people[i]:                                                         #Looping through individual scores
        if (j == 0) and ( (people[i])[j] == 3):
            project1.append(people[i]);
        if (j == 1) and ( (people[i])[j] == 3):
            project2.append(people[i]);
        if (j == 2) and ( (people[i])[j] == 3):
            project3.append(people[i]);
        if (j == 3) and ( (people[i])[j] == 3):
            project4.append(people[i]);
        if (j == 4) and ( (people[i])[j] == 3):
            project5.append(people[i]);

#Validation
print(projectList);
'''

'''
for i in person1:
    if (i == 0 and person1[i] == 3):
        project1.append("person1");
    if (i == 1 and person1[i] == 3):
        project2.append("person1");
    if (i == 2 and person1[i] == 3):
        project3.append("person1");
    if (i == 3 and person1[i] == 3):
        project4.append("person1");
    if (i == 4 and person1[i] == 3):
        project5.append("person1");
'''

''' Relic Code
for i in person1:
    if i == 0:
        if person1[i] == 3:
            project1.append("person1");
        elif i == 1:
            if person1[i] == 3:
                project2.append("person1");
        elif i == 2:
            if person1[i] == 3:
                project3.append("person1");
        elif i == 3:
            if person1[i] == 3:
                project4.append("person1");
        elif i == 4:
            if person1[i] == 3:
                project5.append("person1");
'''
#print(project4);
