# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:46:50 2021

@author: Shashwat Sparsh
"""
import random;

#Class Declarations
class Student:
    def __init__(self, name):
        self.name = name
        self.projectPreferences = list()
        self.skills = list()
        self.currentAffinityScore = 0;
        self.affinityScores = list();
        self.primaryPreference = 1;    
    
    def getName(self):
        return self.name
    
    def getSkills(self):
        return self.skills
    
    def setSkills(self, skills):
        self.skills = skills
    
    def setPrimaryPreference(self, preference1):
        self.primaryPreference = preference1

    def setPreferences(self, preferences):
        self.projectPreferences = preferences
    
    def getPreferences(self):
        return self.projectPreferences
        
    def getAffinityScores(self):
        return self.affinityScores
    
    def setAffinityScores(self,affinityScores):
        self.affinityScores = affinityScores
    
    def getCurrentAffinityScore(self):
        return self.currentAffinityScore
    
    def setAffinityScore(self, score):
        self.currentAffinityScore = score
    
    def __str__(self):
        return "\n \t" + str(self.name) + " " + str(self.projectPreferences) + " " + str(self.currentAffinityScore)
    
    def __repr__(self):
        return str(self)


class Project:
    def __init__(self, number, maxCount):
        self.number = number
        #self.name = name
        self.maxCount = maxCount
        self.roster = list()
        self.affinityCoefficients = list()
    
    def getNumber(self):
        return self.number
    
    def getMaxCount(self):
        return self.maxCount
    
    def setMaxCount(self, count):
        self.maxCount = count        
    
    def addStudent(self, Student):
        self.roster.append(Student)
    
    def removeStudent(self, Student):
        self.roster.remove(Student)
    
    def getRoster(self):
        return self.roster
    
    def getRosterCount(self):
        rosterCount = len(self.getRoster)
        return rosterCount
    
    def getSpace(self):
        space = self.getRosterCount() - self.getMaxCount()
        return space
    
    def setAffinityCoefficients(self, Coefficients):
        self.affinityCoefficients = Coefficients
    
    def getAffinityCoefficients(self):
        return self.affinityCoefficients
    
    def __str__(self):
        return "\n" + str(self.number) + " " + str(self.roster)

    def __repr__(self):
        return str(self)#str(self.number) + " " + str(self.roster)

#End
        
#Difference Function
def emptiestProject(projectList):
    comparator = 0;
    for i in range(len(projectList)):
        currentProject = projectList[i];
        size = currentProject.getRosterCount;        
        maxCount = currentProject.getMax;
        emptySpace = maxCount - size;
        if (emptySpace > comparator):
            emptiestProject = currentProject;
    return emptiestProject;

'''        
def randomSwap(Project1, projectList):
    proj1Size = Project1.getRosterCount;
    studentIndex = random.randint(0,Proj1Size);
    student.
'''

def swapToSecond(Student, Project):
    preferences = student.getPreferences();
    secondPreference = preferences[1];
    