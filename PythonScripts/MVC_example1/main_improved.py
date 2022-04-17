# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 09:40:11 2022

@author: Владислав
"""

import tkinter as tk
from tkinter import ttk
import marketlist as mkl


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='clienticon.ico')
        tk.Tk.wm_title(self, 'Farmers Markets')
        tk.Tk.wm_minsize(self, 800, 600)

        container = tk.Frame(master=self)
        container.pack(side='top', fill='both', expand='true')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Переменные
        self.search_options = ('Опция 1', 'Опция 2', 'Опция 3')
        self.radius_options = ('10', '20', '40', '80', '∞')
        self.sorting_options = ('Опция сортировки 1', 'Опция сортировки 2')

        self.search_option = tk.StringVar(self)
        self.radius_option = tk.StringVar(self)
        self.sorting_option = tk.StringVar(self)
        self.search_text = tk.StringVar(self)  # Переменная для текстового поля
        self.search_option.set(self.search_options[0])
        self.radius_option.set(self.radius_options[0])
        self.sorting_option.set(self.sorting_options[0])

        self.selected_market = tk.StringVar(self)

        # Cловарь с фреймами
        self.frames = {}
        for F in (MainPage, DetailsPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def search_set(self, option):
        print(f'Опция поиска: {option}')

    def sorting_set(self, option):
        print(f'Опция сортировки: {option}')

    def radius_set(self, option):
        print(f'Радиус поиска: {option}')
        #print(f'Также вместо переданного значения str можно прочитать переменную в объекте класса: {self.search_radius.get()}')

    def find(self):
        print(f'Поиск "{self.search_text.get()}"')

    def sort(self):
        print(f'Сортировка по {self.sorting_option.get()}')
    
    def btntest(self, arg):
        print(f'Нажата кнопка подробностей элемента {arg}')
        self.selected_market.set(arg)
        self.show_frame(DetailsPage)
        

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Вызов в Application: frame = MainPage(container, self)
        # parent - контейнер-родитель (просто фрейм в Application)
        # на его основе создаем этот фрейм, уже с содержимым
        # controller - приложение-родитель, то есть сам Application.
        # Там хранятся все переменные. Поэтому обращение к ним идет в виде
        # controller.<имя поля>. Например, controller.search_text
        
        # Конфигурируем сетку
        tk.Frame.grid_rowconfigure(self, 0, weight=0)
        tk.Frame.grid_rowconfigure(self, 1, weight=0)
        tk.Frame.grid_rowconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        # Поле поиска
        ent_search = tk.Entry(self, foreground='red', width=50, textvariable=controller.search_text)
        ent_search.insert(0, 'Поле поиска')
        ent_search.grid(row=0, column=0, pady=10, padx=5, sticky=tk.E+tk.W)
        # Выбор параметра поиска, установка начального значения
        search_dropdown = tk.OptionMenu(self,
                                        controller.search_option,
                                        *controller.search_options,
                                        command=controller.search_set)
        search_dropdown.grid(row=0, column=1, sticky=tk.E+tk.W)
        # Выбор радиуса поиска, установка начального значения
        radius_dropdown = tk.OptionMenu(self,
                                        controller.radius_option,
                                        *controller.radius_options,
                                        command=controller.radius_set)
        radius_dropdown.grid(row=0, column=2, sticky=tk.E+tk.W)
        # Кнопка поиска
        btn_find = tk.Button(self, text='Найти!', command=controller.find)
        btn_find.grid(row=0, column=3, sticky=tk.E+tk.W)
        # Выбор опции сортировки
        sorting_dropdown = tk.OptionMenu(self,
                                         controller.sorting_option,
                                         *controller.sorting_options,
                                         command=controller.sorting_set)
        sorting_dropdown.grid(row=1, column=0, sticky=tk.E+tk.W)
        # Кнопка сортировки
        btn_sort = tk.Button(self, text='Сортировать', command=controller.sort)
        btn_sort.grid(row=1, column=1, sticky=tk.E+tk.W)
        # Поле данных
        # Создаем фрейм в ячейке сетки, состоящий из canvas и скролл бара
        # В canvas помещаем еще один фрейм, и в нем создаем окно, в которое
        # и будем помещать записи
        outer_data_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        outer_data_frame.grid(row=2, column=0, columnspan=4, sticky='nsew')
        data_canvas = tk.Canvas(master=outer_data_frame)
        data_scrollbar_y = tk.Scrollbar(master=outer_data_frame, orient=tk.VERTICAL, command=data_canvas.yview)
        data_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        data_canvas.configure(yscrollcommand=data_scrollbar_y.set)
        data_canvas.bind('<Configure>', lambda e: data_canvas.configure(scrollregion = data_canvas.bbox('all')))
        data_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        data_frame = tk.Frame(master=data_canvas)
        data_canvas.create_window((0,0), window=data_frame, anchor='nw')
        
        market_list = mkl.MarketList(data_frame, controller)
        market_list.grid(row=0, column=0)

# class MainPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(master=self, text='Main page')
#         label.pack(pady=20, padx=20)
#         # Нужно использовать lambda, так как если писать напрямую
#         # command = controller.show_frame(DetailsPage) произойдет вызов
#         # метода show_frame с аргументом, которого не существует
#         btn1 = tk.Button(master=self, text='Show details',
#                          command=lambda: controller.show_frame(DetailsPage))
#         btn1.pack()

# class MarketItem(tk.Frame):
#     def __init__(self, parent, controller, content):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(master=self)
#         label.pack(pady=20, padx=20)
#         btn1 = ttk.Button(master=self, text='Show details',
#                          command=lambda: controller.show_frame(DetailsPage))
#         btn1.pack()

class DetailsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(master=self, textvariable=controller.selected_market)
        label.pack(pady=20, padx=20)
        btn1 = ttk.Button(master=self, text='Go to main',
                          command=lambda: controller.show_frame(MainPage))
        btn1.pack()


if __name__ == '__main__':
    app = Application()
    app.mainloop()