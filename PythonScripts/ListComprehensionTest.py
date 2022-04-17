# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 17:37:44 2022

@author: Владислав
"""


# mylist = [i*i for i in range(0, 10) if i % 2 == 1]
mylist = [i*i for i in range(0, 10) if i > 5]
print(mylist)
mylist2 = [[i for i in range(0, 5)] for j in range(0, 5)]
print(mylist2)
mylist3 = [(i, j) for i in range(0, 5) for j in range(0, 5) if i == j]
print(mylist3)
mylist4 = [i*j for i in range(0, 5) for j in range(0, 5) if i == j]
print(mylist4)