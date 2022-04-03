# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:57:25 2022

@author: Владислав
"""


from random import randint  # Импорт одного имени (в данном случае - функции)
import time


def cube_game(name1, name2):
    sum1, sum2 = 0, 0  # Сумма очков первого и второго игроков
    # Моделирование бросания кубика первым играющим
    print('Кубик бросает', name1)
    for i in range(5):
        time.sleep(2)
        n1 = randint(1, 6)
        print('Выпало:', n1)
        sum1 += n1
    # Моделирование бросания кубика вторым играющим
    print('Кубик бросает', name2)
    for i in range(5):
        time.sleep(2)
        n2 = randint(1, 6)
        print('Выпало:', n2)
        sum2 += n2
    return [sum1, sum2]
