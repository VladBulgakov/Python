# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 00:54:36 2022

@author: Владислав
"""


# Функция возвращает значение из файла, связанное с ключом
def keyval(key):
    keywords = []
    with open('config.txt', encoding='utf-8') as file:
        filecontent = file.read().split("\n")
        for line in filecontent:
            keypair = line.split('=')
            if not keypair[0] == '':
                keywords.append(keypair)
        for item in keywords:
            if item[0] == key:
                return item[1]
        return
