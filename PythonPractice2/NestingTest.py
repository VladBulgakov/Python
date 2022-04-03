# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:07:39 2022

@author: Владислав
"""

#Вложенность данных
rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'},\
       'job': ['dev', 'mgr'], 'age': 25}
    
print(rec['name'])
print(type(rec['name']))
print(rec['name']['firstname'])
print(type(rec['name']['firstname']))

#вывод полного имени
print(f"Полное имя {rec['name']['firstname']} {rec['name']['lastname']}")

#Добавление элемента и вывод списка должностей
rec['job'].append('eng')
for x in rec['job']:
    print(x) 

#Вывод полной информации
#Как вывести в строку содержимое rec?
print(f"Полное имя {rec['name']['firstname']} {rec['name']['lastname']} "
      +f"Возраст {rec['age']} " + f"Должности {rec['job']}")

print(rec.get('job'))