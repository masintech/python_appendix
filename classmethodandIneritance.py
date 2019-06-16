#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 00:43:12 2019

@author: marcus
"""

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks)/len(self.marks)
    
    @classmethod
    def friend(cls, origin,friend_name,*args, **kwargs):
        return cls( friend_name,origin.school,*args, **kwargs)

class WorkingStudent(Student):
    def __init__(self,name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent("Greg","Oxford",120.0,"Software Developer")
print(anna.salary)


friend1 = WorkingStudent.friend(anna,"Ted", salary = 15.0, job_title="Software Architecture")
friend2 = WorkingStudent.friend(anna,"Terry",  15.0, "Software Architecture")

print(friend1.name)
print(friend1.school)
print(friend1.salary)
print(friend1.job_title)


print(friend2.name)
print(friend2.school)
print(friend2.salary)
print(friend2.job_title)