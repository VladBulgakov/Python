# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:15:42 2022

@author: Владислав
"""

import tkinter as tk

root = tk.Tk()
root.title('Main window')
root.geometry('600x400')

# Создаем фрейм на все окно, в котором все будет храниться
main_frame = tk.Frame(master=root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Создаем canvas, чтобы привязать к нему скроллбары
main_canvas = tk.Canvas(master=main_frame)

# Добавляем скроллбары для canvas
main_scrollbar_y = tk.Scrollbar(master=main_frame, orient=tk.VERTICAL, command=main_canvas.yview)
main_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
main_scrollbar_x = tk.Scrollbar(master=main_frame, orient=tk.HORIZONTAL, command=main_canvas.xview)
main_scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

#Конфигурируем canvas
main_canvas.configure(xscrollcommand=main_scrollbar_x.set, yscrollcommand=main_scrollbar_y.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion = main_canvas.bbox('all')))

# Добавляем canvas в фрейм
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Создаем фрейм, связанный с canvas
inner_frame = tk.Frame(master=main_canvas)

# Создаем окно внутри canvas, и добавляем туда inner_frame
main_canvas.create_window((0,0), window=inner_frame, anchor='nw')

for i in range(0,100):
    for j in range(1,20):
        btn = tk.Button(master=inner_frame, text=f'Button {i}').grid(row=i,column=j, padx=10, pady=10)

root.mainloop()