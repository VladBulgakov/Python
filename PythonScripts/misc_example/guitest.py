# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:23:35 2022

@author: Владислав
"""

import tkinter as tk

window = tk.Tk()
star = tk.PhotoImage(file='star.png')
greeting = tk.Label(text="Привет, Tkinter!", foreground='blue', background='white')
greeting.pack()
img = tk.Label(image=star, width=250, height=250)
img.pack()
entfield = tk.Entry(foreground='red', width=50)
entfield.insert(0,'hi')
entfield.pack()
mybtn = tk.Button(text='Нажми меня!', background='light blue')
mybtn.pack()
mytb = tk.Text()
mytb.pack()
# рамка может быть контейнером для виджетов
myframe = tk.Frame(relief = tk.RIDGE, borderwidth=5)
flabel1 = tk.Label(text='Текст в лейбле в фрейме', background='orange', master=myframe)
flabel2 = tk.Label(text='Это лейбл 2', background='orange', master=myframe)
flabel1.pack()
flabel2.pack(side=tk.LEFT)
myframe.pack()
#Заполнение: frame3.pack(fill=tk.X)
#расположение элемента pack(fill=tk.Y, side=tk.LEFT)
#есть еще fill=tk.Y и tk.BOTH
window.mainloop()
print('exit')