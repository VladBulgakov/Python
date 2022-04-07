# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:09:55 2022

@author: Владислав
"""

import PizzaModule

pname = 'Барбекю'

bbq_prices = {'Маленькая': 250,
              'Средняя': 300,
              'Большая': 350,
              'Гигант': 400}


class bbq(PizzaModule.pizza):
    def __init__(self, size_name='Средняя', dough_name='Классическое',
                 is_spicy=False, with_greenery=True):
        super().__init__(size_name=size_name,
                         dough_name=dough_name)
        self.spicy = is_spicy
        self.greenery = with_greenery
        self.price = bbq_prices[size_name]

    def __str__(self):
        if self.spicy is True:
            if self.greenery is True:
                return f'{super().__str__()}\n'\
                       'Начинка "Барбекю", острая, с зеленью\n'\
                       f'Цена {self.price} рублей'
            else:
                return f'{super().__str__()}\n'\
                        'Начинка "Барбекю", острая\n'\
                        f'Цена {self.price} рублей'
        else:
            if self.greenery is True:
                return f'{super().__str__()}\n'\
                       'Начинка "Барбекю", с зеленью\n'\
                       f'Цена {self.price} рублей'
            else:
                return f'{super().__str__()}\n'\
                        'Начинка "Барбекю"\n'\
                        f'Цена {self.price} рублей'
