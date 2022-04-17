# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:11:27 2022

@author: Владислав
"""

# OptionMenu(
#     master, 
#     variable, 
#     value, 
#     *values, 
#     **kwargs
#     )

# master is the window on which you want to place the OptionMenu. It can be the main window, secondary window or frame.
# variable means the value of the widget is not fixed, it will keep on changing. the variable can be implemented on the following:
# StringVar() – Holds a string; default value “”
# IntVar() – Holds an integer; default value 0
# DoubleVar() – Holds float value; default value 0.0
# BooleanVar() – Holds a boolean, returns 0 for False and 1 for True
# value depends upon the type of variable, if a variable is StringVar() then the value will be any name or set of characters.
# *value is the name of the list in which we have stored all the options.

# При вызове функции можно использовать оператор * для распаковки итерируемого объекта в аргументы вызова:

# >>> fruits = ['lemon', 'pear', 'watermelon', 'tomato']
# >>> print(fruits[0], fruits[1], fruits[2], fruits[3])
# lemon pear watermelon tomato
# >>> print(*fruits)
# lemon pear watermelon tomato

# Строка print(*fruits) передаёт все элементы списка fruits в вызов print() как отдельные аргументы, 
# поэтому нам даже не нужно знать, сколько элементов в списке.
# Здесь оператор * — не просто синтаксический сахар. Без фиксированной длины списка
#  было бы невозможно передать элементы итерируемого объекта как отдельные аргументы, не используя *

import tkinter as tk

window = tk.Tk()
window.title('Droddownlist-PythonGuides')
window.geometry('400x300')
window.config(bg='#F2B90C')

# display_selected(choice): - в примере так, хз зачем
def display_selected(choice):
    choice = variable.get()
    print(choice)

countries = ['Bahamas','Canada', 'Cuba','United States']

# Создаем переменную, в которой хранится выбор. Читаем ее в обработчике
variable = tk.StringVar()
variable.set(countries[0]) #устанавливаем начальное значение

# creating widget
dropdown = tk.OptionMenu(
    window,
    variable,
    *countries,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

# infinite loop 
window.mainloop()