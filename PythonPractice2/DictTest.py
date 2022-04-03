# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:52:55 2022

@author: Владислав
"""

D = {'food': 'Apple', 'quantity': 4, 'color': 'Red'}
print(D['food'])
D['quantity'] += 1
print(D['quantity'])

#Создание и заполнение словаря
A = {}
#Можно ли конвертировать второе значение (возраст) в int в этой же строке?
#Как map, но чтобы к каждому значению применялась своя функция
A['name'], A['age'] = input("Введите имя и возраст: ").split()
print(A["name"])
print(A["age"])