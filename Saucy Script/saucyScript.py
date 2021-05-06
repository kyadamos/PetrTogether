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
    
import saucyScriptClasses
#import random

#Primary Sorting Function

def preferenceConverter(preference):
    switcher = {
            'Project 1':1,
            'Project 2':2,
            'Project 3':3,
            'Project 4':4,
            'Project 5':5,
            'Project 6':6,
            'Project 7':7,
            'Project 8':8,
            'Project 9':9,
            'Project 10':10,
            'Project 11':11,
            'Project 12':12,
            'Project 13':13,
            'Project 14':14,
            'Project 15':15,
            }
    return switcher.get(preference, "Invalid Preference")

#End

import numpy as np;
#import tinkter as tk;
import pandas as pd;

numProjects = 15;
projectList = list();
studentList = list();
projectPreferences = list();

for currentProjectNum in range(1,16):    
    #print(currentProjectNum);
    projectList.append(saucyScriptClasses.Project(currentProjectNum, 6));

    
data = pd.read_csv (r'D:\Documents\GitHub\PetrTogether\Saucy Script\F20_dataModified.csv')   
df = pd.DataFrame(data, columns= ['Student number','Preference 1', 'Preference 2', 
                                  'Preference 3', 'Preference 4', 'Preference 5', 
                                  'Mechanical Skills', 'Electronics', 'Welding',
                                  'Metal Machining', 'Woodworking', 'Power Tools',
                                  '3D Printing', 'Laser Cutting']);

#print(df);


numStudents = len(df) - 1;

#Create Student List
for i, row in df.iterrows():
    #Create Student Object
    student = row.values[0];
    currentStudent = saucyScriptClasses.Student(student);
    #Pull Relevant data for Preferences and Skills
    projectPreferences = (preferenceConverter(row.values[1]), preferenceConverter(row.values[2]),
                          preferenceConverter(row.values[3]), preferenceConverter(row.values[4]),
                          preferenceConverter(row.values[5]));
    skills = (row.values[6], row.values[7], row.values[8], row.values[9],
              row.values[10], row.values[11], 3, row.values[13]);
    
    #row.values[12]
    #Set Student Preferences and Skills
    currentStudent.setPreferences(projectPreferences);
    currentStudent.setSkills(skills);
    #Add Student to list
    studentList.append(currentStudent);

#Sort into Primary Preferences    
for currentStudentNum in range(len(df)):
    currentStudent = studentList[currentStudentNum];
    preferences = currentStudent.getPreferences();
    #print(preferences[0]);
    proj = projectList[preferences[0] - 1];
    proj.addStudent(currentStudent);
    #print(proj);
    #if currentStudentNum == 0:
        #print(preferences);

projectList[0].setAffinityCoefficients([.15, .15, .05, .05, .15, .15, .15, .15]); #UAV Forge
projectList[1].setAffinityCoefficients([.05, .05, .05, .1, .2, .15, .2, .2]);
projectList[2].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[3].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[4].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[5].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[6].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[8].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[9].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[10].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[11].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[12].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[13].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);
projectList[14].setAffinityCoefficients([.1, .1, .05, .05, .1, .1, .1, .1]);

#Automate this by importing as df
projectList[0].setMaxCount(6);
projectList[1].setMaxCount(5);
projectList[2].setMaxCount(5);
projectList[3].setMaxCount(5);
projectList[4].setMaxCount(5);
projectList[5].setMaxCount(4);
projectList[6].setMaxCount(5);
projectList[7].setMaxCount(5);
projectList[8].setMaxCount(4);
projectList[9].setMaxCount(4);
projectList[10].setMaxCount(4);
projectList[11].setMaxCount(4);
projectList[12].setMaxCount(6);
projectList[13].setMaxCount(5);
projectList[14].setMaxCount(4);

#'''
for i in range(len(projectList)):
    currentProject = projectList[i];
    currentAffinityCoefficients = currentProject.getAffinityCoefficients();
    currentRoster = currentProject.getRoster();
    for j in range(len(currentRoster)):
        currentStudent = currentRoster[j];
        currentSkillSet = currentStudent.getSkills();
        currentAffinityScore = sum(np.multiply(currentAffinityCoefficients, currentSkillSet));
        currentStudent.setAffinityScore(currentAffinityScore());
    #print(currentRoster);
    #break

#'''

#Project Student Table = pd.DataFrame
#print(projectList[0]);
#print(studentList[0]);
#proj = projectList[0];
#print(proj);

'''
skillset = (studentList[0]).getSkills();
print(skillset);
currentProject = projectList[0];
currentAffinityCoefficients = currentProject.getAffinityCoefficients();
currentRoster = currentProject.getRoster();
currentStudent = currentRoster[0];
currentSkillSet = currentStudent.getSkills();
currentAffinityScore = sum(np.multiply(currentAffinityCoefficients, currentSkillSet));
#print(currentAffinityScore);
currentStudent.setAffinityScore(currentAffinityScore);
print(currentStudent.getCurrentAffinityScore());
'''


''' Framework For Automated Assignment and Comparison

Project Loop:
    curentProject = Project[i]
    if Project[i].getMaxCount < len(Project[i].getRoster):       
        loopCount = 1000;
        currentLowestScore = 1000
        currentMoveStudent = Student(placeholder)
        Roster Loop:
            currentStudent = roster[j] 
            currentScore = currentStudent.getAffinityScore
            if (currentScore < currentLowestScore):
                currentSwapStudent = currentStudent
        secondaryPref = currentSwapStudent.getPreferences()[1]
        ProjectList[secondaryPref - 1].append(currentMoveStudent)
        
'''






















'''
for studentNum in range(len(studentList)):
    currentStudent = studentList[studentNum];
    currentPreference = curentStudent.getPreferences();
'''

'''
for i in range(len(projectList)):
    proj = projectList[i];
    limit = proj.getMaxCount();
    currentRoster = proj.getRoster();
    rosterCount = len(currentRoster);
    if rosterCount > limit:
        mvStudent = currentRoster[4];   #randint(0, rosterCount)
        2ndpref = mvStudent.getPreferences();
        if (project)
        print(2ndpref);
    
#print(len(projectList));
'''