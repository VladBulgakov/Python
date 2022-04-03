# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:59:15 2022

@author: Владислав
"""


import name_input
import game_core
import winner

# Ввод имен играющих
igrok1, igrok2 = name_input.name_input()
# Игра
sum1, sum2 = game_core.cube_game(igrok1, igrok2)
# Определение результата
winner.print_winner(igrok1, sum1, igrok2, sum2)
input()
