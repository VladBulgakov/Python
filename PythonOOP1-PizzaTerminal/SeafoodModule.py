# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:09:55 2022

@author: Владислав
"""

import PizzaModule

pname = 'Дары моря'

seafood_prices = {'Маленькая': 320,
                  'Средняя': 380,
                  'Большая': 450,
                  'Гигант': 500}


class seafood(PizzaModule.pizza):
    def __init__(self, size_name='Средняя', dough_name='Классическое',
                 with_greenery=False):
        super().__init__(size_name=size_name,
                         dough_name=dough_name)
        self.greenery = with_greenery
        self.price = seafood_prices[size_name]

    def __str__(self):
        if self.greenery is True:
            return f'{super().__str__()}\nНачинка "Дары моря" с зеленью\n'\
                    f'Цена {self.price} рублей'
        else:
            return f'{super().__str__()}\nНачинка "Дары моря"\n'\
                    f'Цена {self.price} рублей'
