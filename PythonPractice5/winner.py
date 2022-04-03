# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:58:40 2022

@author: Владислав
"""


def print_winner(name1, sum1, name2, sum2):
    if sum1 > sum2:
        print('Выиграл', name1)
    elif sum1 < sum2:
        print('Выиграл', name2)
    else:
        print('Ничья')
