# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:29:31 2022

@author: Владислав
"""
# Базовый класс "Пицца"

import time
import copy

dough_types = {'Тонкое': 'thin',
               'Классическое': 'classic',
               'Сырный бортик': 'cheeseborder'}
pizza_sizes = {'Маленькая': 15,
               'Средняя': 30,
               'Большая': 35,
               'Гигант': 40}


# Функция поиска ключа в словаре по значению
def findkey(dictionary, value_to_find):
    k = ''
    for key, value in dictionary.items():  # пары ключ-значение
        if value == value_to_find:
            k = key
    if k == '':
        return None
    else:
        return k


class pizza:
    def __init__(self, size_name='Средняя',
                 dough_name='Классическое'):
        self.size = pizza_sizes[size_name]
        self.dough = dough_types[dough_name]
        # приватный атрибут __cooked, который можно изменить и прочитать
        # толкьо через метод. Метод работает 3 секунды
        self.__cooked = False
        # цена переопределяется в классах-наследниках, но
        # является атрибутом базового класса (по умолчанию - 1 рубль)
        self.price = 1

    def _valid_pizza(self):
        if findkey(dough_types, self.dough) is not None\
                and findkey(pizza_sizes, self.size) is not None:
            return True
        else:
            return False

    def cook(self):
        if self.__cooked is not True and self._valid_pizza() is True:
            print('Началось приготовление пиццы...')
            time.sleep(3)
            self.__cooked = True
            print('Пицца готова!')
        elif self._valid_pizza() is not True:
            print('Пицца сконфигурирована неверно, и поэтому не была приготовлена')
        else:
            print('Пицца уже готова!')

    def iscooked(self):
        return self.__cooked

    def __str__(self):
        if self._valid_pizza() is not True:
            return 'Данная пицца сконфигурирована неверно. '\
                    'Ниже приведены значения ее атрибутов\n'\
                    f'{self.__repr__()}'
        if self.__cooked is True:
            return f'Пицца размером {self.size} см '\
                    f'на тесте "{findkey(dough_types, self.dough)}"'
        else:
            return f'Пицца размером {self.size} см '\
                    f'на тесте "{findkey(dough_types, self.dough)}" '\
                    f'(Еще не готова)'

    def __repr__(self):
        return f'size = {self.size}; dough = {self.dough}; '\
              f'__cooked = {self.__cooked}'

    def _privatefun(self):
        print('Это приватный метод!')

    def __veryprivatefun(self):
        print('Это приватный метод, который можно вызвать от имени класса')

    def __add__(self, other):
        print('Сумма любых двух пицц создает пиццу-гигант с начинкой как у '
              'первого аргумента, тестом как у второго, и средней ценой '
              'двух пицц')
        new_pizza = copy.deepcopy(self)
        new_pizza.size = pizza_sizes['Гигант']
        new_pizza.dough = other.dough
        new_pizza.price = int((self.price + other.price)/2)
        return new_pizza
