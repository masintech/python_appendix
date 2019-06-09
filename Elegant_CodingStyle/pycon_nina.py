#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:34:11 2019

@author: marcus
"""

class IterableServer:
    
    def __init__(self):
        
my_gen = (num for num in range(1))
my_gen
# raise StopIteration when there are no more elements
next(my_gen)


class Operations:
    def say_hi(self, name):
        print('Hello', name)
        
    def say_bye(self, name):
        print('Goodbye', name)
    
    def default(self, arg):
        print('This operation is not supported')

if __name__=='__main__':
    operations = Operations()
    
    command, argument = input('> ').split()
    getattr(operations, command, operations.default)(argument)
    
    int('10010', base=2)
    
    from functools import partial
    basetwo = partial(int, base=2)
    basetwo
    basetwo('10010')
    # 19:30 Youtube Video
    # title: Nina Zakharenko - Elegant Solutions For Everyday Python Problems - PyCon 2018

    