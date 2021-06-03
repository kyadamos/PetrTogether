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
from saucyScriptClasses import findEmptiestProject
import numpy as np;
#import tinkter as tk;
import pandas as pd;

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

numProjects = 15;
projectList = list();
studentList = list();
projectPreferences = list();

#Read Student Data  
data = pd.read_csv (r'.\F20_Test.csv')   
df = pd.DataFrame(data, columns= ['Student number','Preference 1', 'Preference 2', 
                                  'Preference 3', 'Preference 4', 'Preference 5', 
                                  'Mechanical Skills', 'Electronics', 'Welding',
                                  'Metal Machining', 'Woodworking', 'Power Tools',
                                  '3D Printing', 'Laser Cutting']);
#print(df);

#Read Project MaxCount Data
maxCountData = pd.read_csv(r'.\Team_size_constraints.csv')
maxCountDF = pd.DataFrame(maxCountData, columns = ['Project Number','F20','W21'])
#print(maxCountDF)
for currentProjectNum, row in maxCountDF.iterrows():
    #print(row.values[1])
    currentProject = saucyScriptClasses.Project(currentProjectNum + 1, row.values[1]);
    projectList.append(currentProject)

#print(projectList[0].getMaxCount())


numStudents = len(df) - 1;
#Create Student List
for i, row in df.iterrows():
    #Create Student Object
    student = row.values[0]
    currentStudent = saucyScriptClasses.Student(student)
    #Pull Relevant data for Preferences and Skills
    projectPreferences = (preferenceConverter(row.values[1]), preferenceConverter(row.values[2]),
                          preferenceConverter(row.values[3]), preferenceConverter(row.values[4]),
                          preferenceConverter(row.values[5]));
    skills = (row.values[6], row.values[7], row.values[8], row.values[9],
              row.values[10], row.values[11], 3, row.values[13]);
    
    #Set Student Preferences and Skills
    currentStudent.setPreferences(projectPreferences)
    currentStudent.setSkills(skills)
    #Add Student to list
    studentList.append(currentStudent)

#Sort into Primary Preferences    
for currentStudentNum in range(len(df)):
    currentStudent = studentList[currentStudentNum]
    preferences = currentStudent.getPreferences()
    #print(preferences[0])
    proj = projectList[preferences[0] - 1]
    proj.addStudent(currentStudent)
    #print(proj);
    #if currentStudentNum == 0:
        #print(preferences);

#Use Numpy random to populate coefficients
coeffSum = 10
numCoeffs = 8
for i in range(len(projectList)):
    randCoeffArray = (np.random.multinomial(coeffSum, np.ones(numCoeffs)/numCoeffs, size=1)[0]) / 10
    projectList[i].setAffinityCoefficients(randCoeffArray)
    
#print(projectList[0].getAffinityCoefficients())
#print(studentList[0].getSkills());
#print(len(projectList[11].getRoster()))

#Set Student Affinity Scores

for h in range(len(studentList)):
    currentStudent = studentList[h]
    currentStudentPreferences = currentStudent.getPreferences()
    skillSet = currentStudent.getSkills()
    #print(skillSet)
    affinityScoreArray = list()
    for i in range(len(currentStudentPreferences)):
        preference = currentStudentPreferences[i]
        projectCoeffs = projectList[preference - 1].getAffinityCoefficients()
        #print(projectCoeffs)
        affinityScore = sum(np.multiply(projectCoeffs, skillSet))
        affinityScore = np.around(affinityScore, 2)
        affinityScoreArray.append(affinityScore)
    #print('')    
    #print(affinityScoreArray)
    currentStudent.setAffinityScores(affinityScoreArray)
    #print(currentStudent.getAffinityScores())
    #print(currentStudent.getAffinityScores())


for a in range(len(projectList)):
    count = 0
    emptiestProject = findEmptiestProject(projectList)
    if (projectList[a].getSpace() < 0):
        roster = projectList[a].getRoster()
        for b, student in enumerate(roster):
            preferencesList = student.getPreferences()
            for c, singlePreference in enumerate(preferencesList):
                if (singlePreference == emptiestProject.getNumber()):
                    emptiestProject.addStudent(student)
                    projectList[a].removeStudent(student)
    count = count + 1
    if (count > 2):
        break;
    




'''
for i in range(len(projectList)):
    currentProject = projectList[i];
    currentAffinityCoefficients = currentProject.getAffinityCoefficients();
    currentRoster = currentProject.getRoster();
    if len(currentRoster) != 0:
        for j in range(len(currentRoster)):
            currentStudent = currentRoster[j];
            currentSkillSet = currentStudent.getSkills();
            print(currentSkillSet)
            print(currentAffinityCoefficients)
            currentAffinityScore = sum(np.multiply(currentAffinityCoefficients, currentSkillSet));
            currentStudent.setAffinityScore(currentAffinityScore);
#'''



'''
#skillset = (studentList[0]).getSkills();
#print(skillset);
currentProject = projectList[16];
currentAffinityCoefficients = currentProject.getAffinityCoefficients();
currentRoster = currentProject.getRoster();
currentStudent = currentRoster[1];
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