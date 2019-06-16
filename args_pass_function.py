#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:06:38 2019

@author: marcus
"""

def my_method(*args):
    return sum(*args)

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    

what_are_kwargs(12,34,56, name="Jose", location="UK")


def info(name,job,salary,bonus,*args, **kwargs):
    print("name: ", name)
    print("job: ", job)
    print("salary: ", salary)
    print("bonus: ", bonus)

info(name='Andy',job='engineer',salary=50,bonus=10)
info('Benny','teacher',3,1)


# filter function 
my_list = [13,2,34,22]
print(list(filter(lambda x: x!= 13, my_list)))

print([x for x in my_list if x !=13])



(lambda x: x*3)(5)

def f(x):
    return x*3
f(5)

