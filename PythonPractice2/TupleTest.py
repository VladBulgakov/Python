# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:40:20 2022

@author: Владислав
"""

print(dir(tuple))
help(tuple.count)


seq = (2,1,8,23,97,92,44,17,39,11,12)
#Число вхождений значения в кортеж
print(seq.count(8))
#Индекс первого попавшегося значения
print(seq.index(44))
print(type(seq))
seqlist = list(seq)
print(type(seqlist))

#Лист можно отредактировать, а кортеж нельзя
seqlist.sort(reverse = True)
seqlist.append("test")
print(seqlist)