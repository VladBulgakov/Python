# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:56:28 2022

@author: Владислав
"""

import math
import statistics
import random

dlist = [2, 5, 1, 0, 6, 8, 7, 7, 7, 4]

#Сумма чисел
dsum = sum(dlist) #Есть еще math.fsum
print(f'Сумма чисел равна {dsum:d}')

#Среднее значение
dmid = statistics.mean(dlist)
print(f'Среднее значение: {dmid:.1f}')

#Расчет медианы
dmed = statistics.median(dlist)
print(f'Медиана: {dmed:.2f}')

#Стандартное отклонение
dstdev = statistics.stdev(dlist)
print(f'Стандартное отклонение: {dstdev:.2f}')

#Генерация случайного числа:
randn = random.randint(0, 100)
print(f'Случайное число: {randn}')