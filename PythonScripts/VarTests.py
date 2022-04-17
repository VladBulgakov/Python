# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:36:17 2022

@author: Владислав
"""

import ImportTest


print(ImportTest.importedval)

# Множество
# set() создает множество из объектов в строке. Порядок одинаковый в одной
# сессии, после перезапуска ядра меняется. Добавление элемента происходит
# не в конец!
tst = set('hello')
tst.add(1)
print(tst)

# Действия с множествами
tst1 = set('hellouser')
res = tst.difference(tst1)  # элементы из tst, не принадлежащие ни одному из tst1
res1 = tst.symmetric_difference(tst1) # элементы, встречающиеся в каждом из множеств, но не встречающиеся в обоих
print(res1)

# Неизменяемое множество frozenset
frz = frozenset('privet')


ImportTest.OpenWebsite('yandex.ru')
