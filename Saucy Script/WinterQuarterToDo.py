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


'''
Affinity Score:
    Categories: [Graphical, Analysis, Presentation, Documentation, Mechanical Fabrication, Electronic/Programming, Welding, Melal Machining, Wood Working, Power Tools, 3D Printing, Laser Cutter]
    UAV Forge:  [.07, .07, .07, .07, .1,.1,.05,.05,.1,.1,.1,.1  ]
    
    Sample Calculation:
    
    Student Skillset = [3, 5, 5, 5, 4, 5, 2, 2, 4, 4, 5, 5]
    UAV Forge = [.07, .07, .07, .07, .1, .1, .05, .05, .1, .1, .1, .1]    
    
    Score = Student Skillset * UAV Forge
          = [(3 * .07) + ... + (5 * .1)]
          = 4.1600
'''
'''
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
'''



'''
for currentStudentNum in range(1, len(df) + 1):
    currentStudent = studentList[currentStudentNum];
    primaryPreference = (currentStudent.getPreferences)[0];
    print(projectList[primaryPreference - 1]);
'''


'''
print(studentList);
print();
print(projectList);
'''














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
