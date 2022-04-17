# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:15:21 2022

@author: Владислав
"""


import logging


def myfun(a='nothing'):
    print(f'You input {a}')
    logging.info(f'Была запущена функция myfun модуля {__name__} с аргументом {a}')
