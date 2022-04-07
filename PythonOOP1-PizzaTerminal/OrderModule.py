# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:24:00 2022

@author: Владислав
"""
# Класс заказа


class order:
    def __init__(self, order_id=0):
        self.id = order_id
        self.foodlist = []

    def add_item(self, item):
        self.foodlist.append(item)

    def calculate_price(self):
        total = 0
        for item in self.foodlist:
            total += item.price
        return total

    def cook(self):
        for item in self.foodlist:
            item.cook()

    def print_receipt(self):
        with open('pizza_receipt.txt', 'w') as file:
            file.write(f'Чек на заказ {self.id}\n')
            for item in self.foodlist:
                file.write(f'{item}\n')
            file.write(f'Сумма заказа {self.id}: {self.calculate_price()}р')

    def clear(self):
        self.foodlist.clear()
