# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:16:45 2022

@author: Владислав
"""
# pip install geopy
# Источник: https://pythonpip.ru/osnovy/geopy-python


from geopy.distance import geodesic
import rus_zip_dal
import rus_zip_core


def process_dist(data):
    zip1 = int(input('Введите почтовый индекс первого отделения: '))
    zip2 = int(input('Введите почтовый индекс второго отделения: '))
    rec1, rec2 = rus_zip_core.record_by_zip(data, zip1),\
        rus_zip_core.record_by_zip(data, zip2)
    print('Расстояние между отделениями:')
    print(f'1) {rec1[0]} ({rec1[1]})')
    print(f'2) {rec2[0]} ({rec2[1]})')
    distance = geodesic([rec1[2], rec1[3]], [rec2[2], rec2[3]]).km
    print(f'{distance:.3f} км')


def process_name(data):
    zip1 = int(input('Введите почтовый индекс отделения: '))
    rec = rus_zip_core.record_by_zip(data, zip1)
    print(f'Название почтового отделения с индексом {rec[0]}:')
    print(f'{rec[1]}')


def process_zip(data):
    name = input('Введите название отделения: ')
    rec = rus_zip_core.record_by_name(data, name)
    print(f'Индекс почтового отделения {rec[1]}:')
    print(f'{rec[0]}')


data = rus_zip_dal.load_data()
command = ''
while command != 'end':
    command = input("Команды ('name', 'zip', 'dist', 'end') => ")
    print(command)
    command = command.strip().lower()
    if command == 'name':
        process_name(data)
    elif command == 'zip':
        process_zip(data)
    elif command == 'dist':
        process_dist(data)
    elif command != 'end':
        print('Команда введена неверно, действие не выполнено')
    print()
print('Работа завершена')
