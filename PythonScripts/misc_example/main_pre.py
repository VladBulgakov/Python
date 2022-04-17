# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:16:31 2022

@author: Владислав
"""

import tkinter as tk


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('800x600')
        self.minsize(800,600)
        self.title('Farmers Markets')
        
        # Опции поиска
        self.search_options = ('ПП1', 'ПП2', 'ПП3')
        self.radius_options = ('10', '20', '40', '80', '∞')
        self.sorting_options = ('Опция сортировки 1', 'Опция сортировки 2')
        # Переменные поиска
        self.search_for = tk.StringVar(self)
        self.search_radius = tk.StringVar(self)
        self.sorting_option = tk.StringVar(self)
        self.search_text = tk.StringVar(self)
        self.search_for.set(self.search_options[0])
        self.search_radius.set(self.radius_options[0])
        self.sorting_option.set(self.sorting_options[0])
        # Инициализация интерфейса
        self.initUI()

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

    def initUI(self):
        # Конфигурация изменения размера окна
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        # Поле поиска
        ent_search = tk.Entry(master=self, foreground='red', width=50, textvariable=self.search_text)
        ent_search.insert(0, 'Поле поиска')
        ent_search.grid(row=0, column=0, pady=10, padx=5, sticky=tk.E+tk.W)
        # Выбор параметра поиска, установка начального значения
        search_dropdown = tk.OptionMenu(self,
                                        self.search_for,
                                        *self.search_options,
                                        command=self.search_set)
        search_dropdown.grid(row=0, column=1, sticky=tk.E+tk.W)
        # Выбор радиуса поиска, установка начального значения
        radius_dropdown = tk.OptionMenu(self,
                                        self.search_radius,
                                        *self.radius_options,
                                        command=self.radius_set)
        radius_dropdown.grid(row=0, column=2, sticky=tk.E+tk.W)
        # Кнопка поиска
        btn_find = tk.Button(master=self, text='Найти!', command=self.find)
        btn_find.grid(row=0, column=3, sticky=tk.E+tk.W)
        # Выбор опции сортировки
        sorting_dropdown = tk.OptionMenu(self,
                                         self.sorting_option,
                                         *self.sorting_options,
                                         command=self.sorting_set)
        sorting_dropdown.grid(row=1, column=0, sticky=tk.E+tk.W)
        # Кнопка сортировки
        btn_sort = tk.Button(master=self, text='Сортировать', command=self.sort)
        btn_sort.grid(row=1, column=1, sticky=tk.E+tk.W)
        # Поле данных
        # Создаем фрейм, состоящий из canvas и скролл бара
        # В canvas помещаем еще один фрейм, и в нем создаем окно, в которое
        # и будем помещать записи
        outer_data_frame = tk.Frame(master=self, relief=tk.RIDGE, borderwidth=5)
        outer_data_frame.grid(row=2, column=0, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W))
        data_canvas = tk.Canvas(master=outer_data_frame)
        data_scrollbar_y = tk.Scrollbar(master=outer_data_frame, orient=tk.VERTICAL, command=data_canvas.yview)
        data_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        data_canvas.configure(yscrollcommand=data_scrollbar_y.set)
        data_canvas.bind('<Configure>', lambda e: data_canvas.configure(scrollregion = data_canvas.bbox('all')))
        data_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        data_frame = tk.Frame(master=data_canvas)
        data_canvas.create_window((0,0), window=data_frame, anchor='nw')
        
        
        for i in range(0,20):
            for j in range(1,20):
                btn = tk.Button(master=data_frame, text=f'Button {i}').grid(row=i,column=j, padx=10, pady=10)


def entry():
    app = MainApp()
    app.mainloop()


if __name__ == '__main__':
    entry()
