# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:21:26 2022

@author: Владислав
"""

import tkinter as tk

# Создает объект окна.
window = tk.Tk()
# Создает обработчик событий.
def handle_keypress(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)

def btn_handler(event):
    print('Кнопка нажата!')

mybtn = tk.Button(text='Нажми меня')
mybtn.pack()
# бинд события
window.bind('<Key>', handle_keypress)
mybtn.bind('<Button-1>', btn_handler)
# Запускает обработчик событий.
window.mainloop()
