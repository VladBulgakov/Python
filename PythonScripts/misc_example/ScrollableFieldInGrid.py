# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:04:08 2022

@author: Владислав
"""

import tkinter as tk

root = tk.Tk()
root.title('Main window')
root.geometry('600x400')


entfield = tk.Entry(master=root, foreground='red', width=50)
entfield.insert(0,'hi')
entfield.grid(row=0, column=0)

# Создаем фрейм на все окно, в котором все будет храниться
data_frame = tk.Frame(master=root)
data_frame.grid(row=1, column=0)

# Создаем canvas, чтобы привязать к нему скроллбары
data_canvas = tk.Canvas(master=data_frame)

# Добавляем скроллбары для canvas
data_scrollbar_y = tk.Scrollbar(master=data_frame, orient=tk.VERTICAL, command=data_canvas.yview)
data_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
data_scrollbar_x = tk.Scrollbar(master=data_frame, orient=tk.HORIZONTAL, command=data_canvas.xview)
data_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

#Конфигурируем canvas
data_canvas.configure(xscrollcommand=data_scrollbar_x.set, yscrollcommand=data_scrollbar_y.set)
data_canvas.bind('<Configure>', lambda e: data_canvas.configure(scrollregion = data_canvas.bbox('all')))

# Добавляем canvas в фрейм
data_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Создаем фрейм, связанный с canvas
inner_frame = tk.Frame(master=data_canvas)

# Создаем окно внутри canvas, и добавляем туда inner_frame
data_canvas.create_window((0,0), window=inner_frame, anchor='nw')

for i in range(0,100):
    for j in range(1,20):
        btn = tk.Button(master=inner_frame, text=f'Button {i}').grid(row=i,column=j, padx=10, pady=10)

root.mainloop()