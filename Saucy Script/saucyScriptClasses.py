# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:46:50 2021

@author: Shashwat Sparsh
"""

#Class Declarations
class Student:
    def __init__(self, name):
        self.name = name
        self.projectPreferences = list()
        
    def getName(self):
        return self.name
    
    def setProjectPreference1(self, preference1):
        self.preference1 = preference1

    def setPreferences(self, preferences):
        self.projectPreferences = preferences
          
    def getPreferences(self):
        return self.projectPreferences
    
    def __str__(self):
        return str(self.name) + str(self.projectPreferences)

class Project:
    def __init__(self, number, maxCount):
        self.number = number
        #self.name = name
        self.maxCount = maxCount
        self.roster = list()
    
    def getMaxCount(self):
        return self.maxCount
    
    def getNumber(self):
        return self.number
    
    def addStudent(self, Student):
        self.roster.append(Student)
    
    def getRoster(self):
        return self.roster;
    
    def __str__(self):
        return str(self.number) + " " + str(self.roster)


#End

#Project Constructor
def projectConstructor(numProjects):
    for count in range(numProjects):
        intString = str(count);
        projectName = "Project " + intString;
        Project(projectName);