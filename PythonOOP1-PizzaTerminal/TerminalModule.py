# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:24:00 2022

@author: Владислав
"""

import PizzaModule as PizM
import PepperoniModule as PepM
import SeafoodModule as SeaM
import BBQModule as BbqM
import OrderModule as OrdM


pizza_names = (f'{PepM.pname}', f'{SeaM.pname}', f'{BbqM.pname}')


def available_pizza():
    print('В меню есть следующие пиццы:')
    for item in pizza_names:
        print(f'"{item}"')


def available_sizes():
    print('Существуют пиццы следующих размеров:')
    for item in PizM.pizza_sizes.items():
        print(f'"{item[0]}" - {item[1]} см')


def available_dough():
    print('Существуют следующие виды теста:')
    for key in PizM.dough_types.keys():
        print(f'"{key}"')

def print_order(order):
    print('Состав вашего заказа:')
    for item in order.foodlist:
        print(item)
    print(f'Сумма заказа: {order.calculate_price()} рублей')


print('>>> Добро пожаловать! <<<')
available_pizza()
available_sizes()
available_dough()
print('Команды терминала: add - добавить пиццу; list - список заказа; '
      'pay - оплатить заказ; drop - отменить заказ и завершить работу')
cmd = ''
order = OrdM.order()
while not cmd == 'drop':
    cmd = input('Введите команду... ')
    if cmd == 'add':
        setup = dict()
        setup['name'] = input('Введите название пиццы... ')
        setup['size'] = input('Введите размер пиццы... ')
        setup['dough'] = input('Введите тип теста... ')
        if setup['name'] not in pizza_names or\
                setup['size'] not in PizM.pizza_sizes or\
                setup['dough'] not in PizM.dough_types:
            print('Неправильная конфигурация!')
            continue
        if setup['name'] == f'{PepM.pname}':
            tmp = input('Вам острую пиццу? Да/Нет ').lower()
            setup['spicy'] = True if tmp == 'да' else False
            new_pizza = PepM.pepperoni(size_name=setup['size'],
                                       dough_name=setup['dough'],
                                       is_spicy=setup['spicy'])
        if setup['name'] == f'{SeaM.pname}':
            tmp = input('Вам пиццу с зеленью? Да/Нет ').lower()
            setup['greenery'] = True if tmp == 'да' else False
            new_pizza = SeaM.seafood(size_name=setup['size'],
                                     dough_name=setup['dough'],
                                     with_greenery=setup['greenery'])
        if setup['name'] == f'{BbqM.pname}':
            tmp = input('Вам пиццу с зеленью? Да/Нет ').lower()
            setup['greenery'] = True if tmp == 'да' else False
            tmp = input('Вам острую пиццу? Да/Нет ').lower()
            setup['spicy'] = True if tmp == 'да' else False
            new_pizza = BbqM.bbq(size_name=setup['size'],
                                 dough_name=setup['dough'],
                                 with_greenery=setup['greenery'],
                                 is_spicy=setup['spicy'])
        order.add_item(new_pizza)
        print('Пицца добавлена!')
    if cmd == 'list':
        print_order(order)
    if cmd == 'pay':
        print('Заказ оплачен!')
        order.cook()
        print_order(order)
        order.print_receipt()
        print('Заказ отправлен. Чек сохранен на диск')
        break
order.clear()
print('Работа завершена!')
input()
