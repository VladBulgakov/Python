# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:23:42 2022

@author: Владислав
"""


from random import randint  # Импорт одного имени (в данном случае - функции)
import time


def name_input():
    name1 = input('Введите имя 1-го играющего ')
    name2 = input('Введите имя 2-го играющего ')
    return [name1, name2]


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


def print_winner(name1, sum1, name2, sum2):
    if sum1 > sum2:
        print('Выиграл', name1)
    elif sum1 < sum2:
        print('Выиграл', name2)
    else:
        print('Ничья')


# Ввод имен играющих
igrok1, igrok2 = name_input()
# Игра
sum1, sum2 = cube_game(igrok1, igrok2)
# Определение результата
print_winner(igrok1, sum1, igrok2, sum2)
input()
