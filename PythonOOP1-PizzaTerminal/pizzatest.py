# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:55:20 2022

@author: Владислав
"""
# Суммирование пицц

import PepperoniModule as PepM
import SeafoodModule as SeaM

mpep = PepM.pepperoni(size_name='Маленькая', dough_name='Классическое')
mpep.cook()
msea = SeaM.seafood(size_name='Большая', dough_name='Сырный бортик')
msea.cook()
print(id(mpep))
print(id(msea))
np = mpep+msea
print(np)
print(id(np))
