# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 11:09:55 2022

@author: Владислав
"""

import PizzaModule

pname = 'Пепперони'

pepperoni_prices = {'Маленькая': 250,
                    'Средняя': 300,
                    'Большая': 350,
                    'Гигант': 400}


class pepperoni(PizzaModule.pizza):
    def __init__(self, size_name='Средняя', dough_name='Классическое',
                 is_spicy=False):
        super().__init__(size_name=size_name,
                         dough_name=dough_name)
        # print(f'>{self.price}') price хранится в базовом классе pizza!
        self.price = pepperoni_prices[size_name]
        self.spicy = is_spicy

    def __str__(self):
        if self.spicy is True:
            return f'{super().__str__()}\nНачинка "Острый пепперони"\n'\
                    f'Цена {self.price} рублей'
        else:
            return f'{super().__str__()}\nНачинка "Пепперони"\n'\
                    f'Цена {self.price} рублей'
