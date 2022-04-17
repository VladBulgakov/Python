# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 08:05:33 2022

@author: Владислав
"""

import tkinter as tk
import confreader as cr
import detailspage as dp
import datalayer as dal
import views as v


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # Вызов в Application: frame = MainPage(container, self)
        # parent - контейнер-родитель (просто фрейм в Application)
        # на его основе создаем этот фрейм, уже с содержимым
        # controller - приложение-родитель, то есть сам Application.
        # Там хранятся все переменные. Поэтому обращение к ним идет в виде
        # controller.<имя поля>. Например, controller.search_text

        # Переменные
        self.data_fields = (['Название', 'MarketName'], ['Город', 'city'],
                            ['Область', 'County'], ['Штат', 'State'],
                            ['Почтовый индекс', 'zip'], ['Рейтинг', 'Rating'])
        self.sorting_directions = (['По возрастанию', 'ASC'],
                                   ['По убыванию', 'DESC'])
        #self.radius_options = (['20 km', 3], ['40 km', 10], ['80 km', 20], ['Не ограничено', None])
        
        self.search_text = tk.StringVar(self)
        self.selected_radius = tk.StringVar(self)
        self.sorting_direction = tk.StringVar(self)
        self.search_field = tk.StringVar(self)
        self.sorting_field = tk.StringVar(self)
        #self.selected_radius.set(self.radius_options[3][0])
        self.sorting_direction.set(self.sorting_directions[0][0])
        self.search_field.set(self.data_fields[0][0])
        self.sorting_field.set(self.data_fields[0][0])
        self.current_page = tk.IntVar(self)
        self.current_page.set(1)
        
        self.loadlist_setup = ['', 'MarketName', 'FMID', 'ASC', None]

        # Конфигурируем сетку
        tk.Frame.grid_rowconfigure(self, 0, weight=0)
        tk.Frame.grid_rowconfigure(self, 1, weight=0)
        tk.Frame.grid_rowconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 0, weight=1)
        tk.Frame.grid_columnconfigure(self, 1, weight=1)
        tk.Frame.grid_columnconfigure(self, 2, weight=1)
        tk.Frame.grid_columnconfigure(self, 3, weight=1)
        # Поле поиска
        ent_search = tk.Entry(self, textvariable=self.search_text)
        ent_search.grid(row=0, column=0, pady=10, padx=5, sticky=tk.E+tk.W)
        # Выбор параметра поиска, установка начального значения
        tmp = [x[0] for x in self.data_fields]
        search_dropdown = tk.OptionMenu(self,
                                        self.search_field,
                                        *tmp)
        search_dropdown.grid(row=0, column=1, sticky=tk.E+tk.W)
        # Выбор радиуса поиска, установка начального значения
        lbl_dist = tk.Label(self, text='Дистанция в км:')
        lbl_dist.grid(row=0, column=2, sticky=tk.E+tk.W)
        ent_radius = tk.Entry(self, textvariable=self.selected_radius)
        ent_radius.grid(row=0, column=3, padx=5, sticky=tk.E+tk.W)
        # Кнопка поиска
        btn_find = tk.Button(self, text='Найти!', command=self.find)
        btn_find.grid(row=0, column=4, rowspan=2, padx=5, sticky='nsew')
        # Выбор опции сортировки
        tmp = [x[0] for x in self.data_fields]
        sorting_dropdown = tk.OptionMenu(self,
                                         self.sorting_field,
                                         *tmp)
        sorting_dropdown.grid(row=1, column=1, sticky=tk.E+tk.W)
        # Выбор направления сортировки
        tmp = [x[0] for x in self.sorting_directions]
        sorting_dropdown = tk.OptionMenu(self,
                                         self.sorting_direction,
                                         *tmp)
        sorting_dropdown.grid(row=1, column=2, columnspan=2, sticky=tk.E+tk.W)
        # Поле данных
        # Создаем фрейм в ячейке сетки, состоящий из canvas и скролл бара
        # В canvas помещаем еще один фрейм, и в нем создаем окно, в которое
        # и будем помещать записи
        outer_data_frame = tk.Frame(self, relief=tk.RIDGE, borderwidth=5)
        outer_data_frame.grid(row=2, column=0, columnspan=5, sticky='nsew')
        data_canvas = tk.Canvas(master=outer_data_frame)
        data_scrollbar_y = tk.Scrollbar(master=outer_data_frame, orient=tk.VERTICAL, command=data_canvas.yview)
        data_scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        data_canvas.configure(yscrollcommand=data_scrollbar_y.set)
        data_canvas.bind('<Configure>', lambda e: data_canvas.configure(scrollregion = data_canvas.bbox('all')))
        data_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # Делаю data_frame полем класса, чтобы иметь к нему доступ в
        # Методах класса (чтобы добавлять в него список ярмарок)
        self.data_frame = tk.Frame(master=data_canvas)
        data_canvas.create_window((0,0), window=self.data_frame, anchor='nw')
        #Список ярмарок в поле с прокруткой
        self.market_list(controller)
        #Индикатор местоположения пользователя:
        lbl_location = tk.Label(self, text = f'Ваше местоположение: x = {cr.keyval("USERPOSX")} y = {cr.keyval("USERPOSY")}')
        lbl_location.grid(row=3, column=0, sticky=tk.E+tk.W)
        #Кнопки переключения страниц
        btn_prev = tk.Button(self, text='Предыдущая страница', command=self.prev_page)
        btn_prev.grid(row=3, column=1, sticky=tk.E+tk.W)
        page_label = tk.Label(self, textvariable=self.current_page)
        page_label.grid(row=3, column=2, sticky=tk.E+tk.W)
        btn_next = tk.Button(self, text='Следующая страница', command=self.next_page)
        btn_next.grid(row=3, column=3, sticky=tk.E+tk.W)

    def market_list(self, controller):
        for content in self.data_frame.winfo_children():
            content.destroy()
        markets = dal.LoadMarketsList(search_text=self.loadlist_setup[0],
                                      search_field=self.loadlist_setup[1],
                                      sorting_field=self.loadlist_setup[2],
                                      sorting_direction=self.loadlist_setup[3],
                                      page=self.current_page.get(),
                                      search_range=self.loadlist_setup[4])
        mlist = v.MarketItemList(self.data_frame, controller, markets)
        mlist.pack(side='top', fill='both', expand='true')

    def next_page(self):
        self.current_page.set(self.current_page.get()+1)
        self.market_list(self.controller)

    def prev_page(self):
        if self.current_page.get() > 1:
            self.current_page.set(self.current_page.get()-1)
        self.market_list(self.controller)

    def find(self):
        try:
            rad = float(self.selected_radius.get())
        except Exception as e:
            rad = None
        self.loadlist_setup = [self.search_text.get(), # Текст запроса
                          [x[1] for x in self.data_fields if x[0] == self.search_field.get()][0],
                          [x[1] for x in self.data_fields if x[0] == self.sorting_field.get()][0],
                          [x[1] for x in self.sorting_directions if x[0] == self.sorting_direction.get()][0],
                          rad
                          ]
        self.market_list(self.controller)