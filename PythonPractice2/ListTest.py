# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:15:58 2022

@author: Владислав
"""

list1 = [82,8,23,97,92,44,17,39,11,12]
print(dir(list))
help(list.insert)
list1.insert(2,0)
print(list1)
list1.append(10)
print(list1)
list1[1], list1[2] = [5,6]
print(list1)
#Удаление элемента инструкцией del
del list1[4]
print(list1)
#Удаление элемента функцией remove - удаляет первый совпадающий элемент
list1.remove(5)
print(list1)
#pop() удаляет элемент по индексу
list1.pop(4)
print(list1)
#сортировка по возрастанию
list1.sort()
print(list1)
#сортировка по убыванию
list1.sort(reverse=True)
print(list1)

#сортировка в отдельный лист
print("----")
list2 = [3,5,6,2,33,6,11]
list3 = sorted(list2)
print(list2)
print(list3)