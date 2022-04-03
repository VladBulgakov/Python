# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:29:55 2022

@author: Владислав
"""


a = 10  # глобальная переменная


def fun1(inp):
    vartest = 1  # переменная для проверки (см. комментарии)
    print(f'>Вы ввели {inp}')

    def innerfun():
        nonlocal inp  # <- попробуй закомментировать эту строку!!!
        # В области видимости вложенной функции находятся аргументы
        # функции, в которую эта функция вложена.
        # inp - переменная-аргумент функции fun1, поэтому ее видно сразу:
        print(f'>>inp равен {inp}')
        # Мы можем обратиться к inp и получить ее значение:
        v = inp
        v += 1
        print(f'>>Значение v: {v}')
        # inp = 0 - ОШИБКА
        # ...но мы не можем изменить inp, не указав, что она не локальная
        # для функции innerfun, поэтому пишем nonlocal inp (строка 17)
        # Таким образом мы указываем, что inp - не локальная переменная
        # для функции innerfun, и ее нужно искать во внешнем пространстве имен.
        # После этого мы можем ее изменить:
        inp += 1
        #
        #
        # При помощи ключевого слова global мы указываем, что переменная a
        # является глобальной (ее поиск начинается сразу в глобальной области
        # видимости). В данном участке кода увеличиваем значение глобальной
        # переменной a на 10:
        global a
        for k in range(1, 11):
            a += 1
        #
        #
        # Пробуем обратиться к локальной переменной vartest функции fun1.
        # Ее не видно даже для чтения:
        # print(f'vartest = {vartest}') - ОШИБКА
        # vartest += 1 - ОШИБКА
        # При помощи ключевого слова nonlocal мы можем указать,
        # что переменная не является локальной. В таком случае осуществляется
        # поиск по имени среди переменных во внешних простанствах имен
        # (в данном случае - в пространстве имен функции fun1)
        # Отличие от global - в случае с global поиск начинается сразу в
        # глобальной области
        nonlocal vartest
        vartest += 1
        print(f'vartest после изменения внутри вложенной функции: {vartest}')
        return v

    # Прибавляем возвращаемое значение v функции innerfun переменной inp.
    # До этого значение inp было изменено внутри вложенной функции! (строка 32)
    inp += innerfun()
    return inp


print(f'Значение a было {a}')
inp1 = 1
print(f'Значение inp1 было {inp1}')
inp1 = fun1(inp1)
print(f'После запуска fun1 inp1 стал равен {inp1}')
print(f'Глобальная a теперь равна {a}')