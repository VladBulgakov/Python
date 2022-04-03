# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:16:20 2022

@author: Владислав
"""

from random import randint #Импорт одного имени (в данном случае - функции)
import time
#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
sum1 = 0 #Сумма очков первого игрока
igrok2 = input('Введите имя 2-го играющего ')
sum2 = 0 #Сумма очков второго игрока
#Моделирование бросания кубика первым играющим
print('Кубик бросает', igrok1)
for i in range(5):
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    sum1 += n1
#Моделирование бросания кубика вторым играющим
print('Кубик бросает', igrok2)
for i in range(5):
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    sum2 += n2
#Определение результата (3 возможных варианта)
if sum1 > sum2:
    print('Выиграл', igrok1)
elif sum1 < sum2:
    print('Выиграл', igrok2)
else:
    print('Ничья')